# Find the titles of workers that earn the highest salary. Output the highest-paid title or multiple titles that share the highest salary.

# worker
# worker_id:int64first_name:objectlast_name:objectsalary:int64joining_date:datetime64[ns]department:object
# title
#worker_ref_id:int64worker_title:objectaffected_from:datetime64[ns]

# Import your libraries
import pandas as pd

# Start writing code
worker.head()

worker_title_df = pd.merge(left=worker,right=title, left_on='worker_id',right_on='worker_ref_id',how='inner')
worker_title_df.head()
worker_title_df['salary_rank'] = worker_title_df['salary'].rank(method='dense',ascending=False)
result = worker_title_df.copy()
result = result[result['salary_rank'] == 1]['worker_title']
result
