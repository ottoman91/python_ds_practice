# Classify each business as either a restaurant, cafe, school, or other. A restaurant should have the word 'restaurant' in the business name. For cafes, either 'cafe', 'café', or 'coffee' can be in the business name. 'School' should be in the business name for schools. All other businesses should be classified as 'other'. Output the business name and the calculated classification.

# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()

# create a function that outputs the values based on the string concatanation
def category(row):
    if row['business_name'].str.contains('restaurant',regex=True):
        val = 'restaurant'
    elif row['business_name'].str.contains('cafe|café|coffee',regex=True):
        val = 'cafe'
    elif row['business_name'].str.contains('School',regex=True):
        val = 'school'
    else:
        val = 'other'
    return val


sf_restaurant_business_category = sf_restaurant_health_violations.copy()
sf_restaurant_business_category['business_type'] = sf_restaurant_business_category.apply(lambda row: category(row), axis=1)
sf_restaurant_business_category = sf_restaurant_business_category[['business_id', 'business_type']]
