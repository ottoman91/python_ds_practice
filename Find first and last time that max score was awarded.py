# Find the first and last times the maximum score was awarded

# Import your libraries
import pandas as pd

# Start writing code
los_angeles_restaurant_health_inspections.head()

# 1. calculate the max score
max_score = los_angeles_restaurant_health_inspections['score'].max()
los_angeles_restaurant_health_inspections['activity_date'] = los_angeles_restaurant_health_inspections['activity_date'].dt.date

first_time = pd.Series(min(los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['score']==max_score]['activity_date'])).to_frame('first_time')

last_time = pd.Series(max(los_angeles_restaurant_health_inspections[los_angeles_restaurant_health_inspections['score']==max_score]['activity_date'])).to_frame('last_time')

pd.concat([first_time,last_time],axis=1)

# select all rows where max_score was awarded.
#dates_with_max_score_df = los_angeles_restaurant_health_inspections.copy()
##dates_with_max_score_df = dates_with_max_score_df[dates_with_max_score_df['score'] == max_score]
#dates_with_max_score_df['activity_date'] = pd.to_datetime(dates_with_max_score_df['activity_date']).dt.date

#max_score_dates_in_ascending_order = dates_with_max_score_df.copy()
#max_score_dates_in_ascending_order = max_score_dates_in_ascending_order.sort_values(by='activity_date',ascending=True)
#max_score_dates_in_descending_order = dates_with_max_score_df.copy()
#max_score_dates_in_descending_order = max_score_dates_in_descending_order.sort_values(by='activity_date',ascending=False)

#first_date_of_max_score = max_score_dates_in_ascending_order.copy()
#first_date_of_max_score = first_date_of_max_score.iloc[:1]['activity_date']


#last_date_of_max_score = max_score_dates_in_descending_order.copy()
#last_date_of_max_score = last_date_of_max_score.iloc[:1]['activity_date']

#first_date_of_max_score = first_date_of_max_score.rename(columns={'activity_date': 'first_time'})

#last_date_of_max_score = last_date_of_max_score.rename(columns={'activity_date': 'last_time'})

#pd.concat([first_date_of_max_score, last_date_of_max_score],axis=1)
