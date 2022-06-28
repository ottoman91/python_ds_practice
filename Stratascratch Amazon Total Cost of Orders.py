# Find the total cost of each customer's orders. Output customer's id, first name, and the total order cost. Order records by customer's first name alphabetically.

# customers
# id, first_name, last_name, city, address, phone_number

# orders
# id, cust_id, order_date, order_details, total_order_cost

import pandas as pd
import numpy as np

dataframe = pd.merge(customers, orders, left_on='id', right_on='cust_id', how='inner')
merged_dataframe = dataframe.groupby(['cust_id', 'first_name'])['total_order_cost'].sum().reset_index()
result = merged_dataframe.sort_values(by='first_name', ascending=True)
