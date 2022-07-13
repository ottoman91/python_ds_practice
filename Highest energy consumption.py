# Find the date with the highest total energy consumption from the Meta/Facebook data centers. Output the date along with the total energy consumption across all data centers.

# fb_eu_energy . date | consumption
# fb_asia_energy
# fb_na_energy


# Import your libraries
import pandas as pd

# Start writing code
fb_eu_energy.head()

# concatanate all of the three dataframes
# group by date and calculate total sum
# use rank function to rank by max
# select rows where rank is max

concatanated_df = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])
concatanated_df = concatanated_df.groupby('date').agg({'consumption':'sum'}).reset_index()
concatanated_df['consumption_rank'] = concatanated_df['consumption'].rank(method='dense',ascending=False)
result = concatanated_df[concatanated_df['consumption_rank'] == 1][['date', 'consumption']]
