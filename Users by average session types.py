#Calculate each user's average session time. A session is defined as the time difference between a page_load and page_exit. For simplicity, assume a user has only 1 session per day and if there are multiple of the same events on that day, consider only the latest page_load and earliest page_exit. Output the user_id and their average session time.

#facebook_web_log
# user_id:int64
# timestamp:datetime64[ns]
# action:object

# Import your libraries
import pandas as pd

# Start writing code
facebook_web_log.head()

# output:
# user_id | page_load | page_exit | session_time

# create a date field for each timestamp

daily_web_logs_df = facebook_web_log.copy()
daily_web_logs_df['date'] = pd.to_datetime(daily_web_logs_df['timestamp']).dt.date

# select all page_loads
all_page_loads_df = daily_web_logs_df.copy()
all_page_loads_df = all_page_loads_df[all_page_loads_df['action']=='page_load']

# select all page_exits
all_page_exist_df = daily_web_logs_df.copy()
all_page_exist_df = all_page_exist_df[all_page_exist_df['action']=='page_exit']

# for all page_loads, group by user_id and date and calculate the latest page_load
all_page_loads_df['page_load_ranking'] = all_page_loads_df.groupby(['user_id','date'])['timestamp'].rank(method='dense',ascending=False)
latest_page_loads_df = all_page_loads_df.copy()
latest_page_loads_df = latest_page_loads_df[latest_page_loads_df['page_load_ranking'] == 1][['user_id','timestamp','date']].rename(columns={'timestamp':'page_load'})

# for all page_exists, find earliest page exit
all_page_exist_df['page_load_ranking'] = all_page_exist_df.groupby(['user_id','date'])['timestamp'].rank(method='dense',ascending=True)
latest_page_exits_df = all_page_exist_df.copy()
latest_page_exits_df = latest_page_exits_df[latest_page_exits_df['page_load_ranking'] == 1][['user_id','timestamp','date']].rename(columns={'timestamp':'page_exit'})

# inner join the two dataframes
merged_df = pd.merge(left=latest_page_loads_df, right=latest_page_exits_df,left_on=['user_id','date'], right_on=['user_id','date'],how='inner')

merged_df['session_time'] = merged_df['page_exit'] - merged_df['page_load']
merged_df['session_time'] = merged_df['session_time'].astype('timedelta64[s]')
# group by user_id and calculate average session time
final_df = merged_df.copy()
final_df = final_df.groupby('user_id').agg({'session_time':'mean'}).reset_index().rename(columns={'session_time':'duration'})
