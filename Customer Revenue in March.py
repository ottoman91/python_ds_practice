# Calculate the total revenue from each customer in March 2019. Include only customers who were active in March 2019.

# Output the revenue along with the customer id and sort the results based on the revenue in descending order.

#orders
#id:int64
# cust_id:int64
# order_date:datetime64[ns]
# order_details:object
# total_order_cost:int64

# Import your libraries
import pandas as pd

# Start writing code

# convert all order_date values to date
orders_date_converted_df = orders.copy()
orders_date_converted_df['order_date'] = pd.to_datetime(orders_date_converted_df['order_date']).dt.date

# select only customers who had orders in march 2019
date_mask = (orders_date_converted_df['order_date'] >= pd.to_datetime('2019-03-01').date()) & (orders_date_converted_df['order_date'] <= pd.to_datetime('2019-03-31').date())

orders_only_in_march_2019_df = orders_date_converted_df.copy()
orders_only_in_march_2019_df = orders_only_in_march_2019_df[date_mask]

#group by customer id and calculate total order
total_revenue_per_customer_df = orders_only_in_march_2019_df.copy()
total_revenue_per_customer_df = total_revenue_per_customer_df.groupby('cust_id').agg({'total_order_cost':'sum'}).reset_index().rename(columns={'total_order_cost':'revenue'})
total_revenue_per_customer_df.sort_values(by='revenue',ascending=False,inplace=True)
total_revenue_per_customer_df
