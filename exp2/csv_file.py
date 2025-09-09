import pandas as pd

df=pd.read_csv("exp2/employees.csv")

print("Employee Details:\n",df)

filtered_df = df[(df['dept']=='CS') & (df['sal']>50000)]

sorted_df =filtered_df.sort_values(by = 'sal',ascending = False)
print("Filtered and sorted employees :\n")

sorted_df.to_csv("filtered_employees.csv",index=False)
