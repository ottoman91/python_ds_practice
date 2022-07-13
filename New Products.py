# You are given a table of product launches by company by year. Write a query to count the net difference between the number of products companies launched in 2020 for the first time with the number of products companies launched in the previous year. Output the name of the companies and a net difference of net products released for 2020 compared to the previous year. If a company is new or had no products in 2019, then any product released in 2020 would be considered as new.

# car launches
# year | company_name | product_name

# Import your libraries
import pandas as pd

# Start writing code
car_launches.head()

# output:
# company_name | net_new_products
# company_name | new_products_2019 | new_products_2020

# 1. group by year and company_name, and calculate distinct product_names

product_launches_per_year = car_launches.copy()

product_launches_per_year = product_launches_per_year.groupby(['year', 'company_name']).agg({'product_name':pd.Series.nunique}).reset_index()
product_launches_per_year.sort_values(by=['company_name', 'year'], ascending=[True,True],inplace=True)
product_launches_per_year['previous_year_launches'] = product_launches_per_year.groupby('company_name')['product_name'].shift()
product_launches_per_year = product_launches_per_year.rename(columns={'product_name': 'current_year_launches'})
product_launches_per_year = product_launches_per_year.fillna(0)
product_launches_per_year['net_new_products'] = product_launches_per_year['current_year_launches'] - product_launches_per_year['previous_year_launches']

result = product_launches_per_year[product_launches_per_year['year'] == 2020][['company_name', 'net_new_products']]
