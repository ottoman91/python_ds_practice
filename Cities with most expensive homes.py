# Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

# zillow_transactions
# id:int64state:objectcity:objectstreet_address:objectmkt_price:int64

# Import your libraries
import pandas as pd

# Start writing code
zillow_transactions.head()
# output: city | names.

# 1. add a column, which has national average.
# 2. national_average.
# 3. group by city and national_average, and calculate the average mkt_price.
# city | city_average | national_average
# 4. select cities where city_average > national_average

national_averages_df = zillow_transactions.copy()
national_averages_df['national_average'] = national_averages_df['mkt_price'].mean()
national_averages_and_city_averages_df = national_averages_df.copy()
national_averages_and_city_averages_df = national_averages_and_city_averages_df.groupby(['city', 'national_average']).agg({'mkt_price':'mean'}).reset_index()
cities_above_national_average = national_averages_and_city_averages_df[national_averages_and_city_averages_df['mkt_price'] > national_averages_and_city_averages_df['national_average']]['city']
