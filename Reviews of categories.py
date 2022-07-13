# Find the top business categories based on the total number of reviews. Output the category along with the total number of reviews. Order by total reviews in descending order.

#yelp_business
# business_id:object
# name:object
# neighborhood:object
# address:object
# city:object
# state:object
# postal_code:object
# latitude:float64
# longitude:float64
# stars:float64
# review_count:int64
# is_open:int64
# categories:object


# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

# output:
# categories | total_reviews

# group by categories
yelp_business_categories = yelp_business.copy()

yelp_business_categories = yelp_business_categories[['review_count','categories']].set_index('review_count').apply(lambda x: x.str.split(';').explode()).reset_index()

yelp_business_categories = yelp_business_categories.groupby(['categories']).agg({'review_count':'sum'}).reset_index().sort_values(by='review_count',ascending=False).rename(columns={'review_count':'total_reviews'})
