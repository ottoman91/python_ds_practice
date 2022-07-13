# Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. If customer had more than one order on a certain day, sum the order costs on daily basis. Output customer's first name, total cost of their items, and the date.

# customers:
#id:int64
# first_name:object
# last_name:object
# city:object
# address:object
# phone_number:object

#orders
#id:int64
#cust_id:int64
#order_date:datetime64[ns]
#order_details:object
#total_order_cost:int64

# Import your libraries
import pandas as pd

# Start writing code

# inner join orders with customers
merged_df = pd.merge(left=orders, right=customers, left_on='cust_id',right_on='id',how='inner')

# convert all order_date to date
merged_df['order_date'] = pd.to_datetime(merged_df['order_date']).dt.date

# group by order_date and cust_id and sum total_order_cost
total_order_cost_per_day_per_cust_df = merged_df.copy()
total_order_cost_per_day_per_cust_df = total_order_cost_per_day_per_cust_df.groupby(['cust_id','first_name', 'order_date']).agg({'total_order_cost':'sum'}).reset_index()
total_order_cost_per_day_per_cust_df.head()

# select all orders between the dates

orders_between_dates_df = total_order_cost_per_day_per_cust_df.copy()

date_mask = (orders_between_dates_df['order_date'] >= pd.to_datetime('2019-02-01').date()) & (orders_between_dates_df['order_date'] <= pd.to_datetime('2019-05-01').date())

orders_between_dates_df = orders_between_dates_df[date_mask]

orders_between_dates_df['order_ranking'] = orders_between_dates_df['total_order_cost'].rank(method='dense',ascending=False)

final_result_df = orders_between_dates_df.copy()
final_result_df = final_result_df[final_result_df['order_ranking']==1]
final_result_df = final_result_df[['first_name', 'order_date', 'total_order_cost']].rename(columns={'total_order_cost':'max_cost'})
final_result_df
