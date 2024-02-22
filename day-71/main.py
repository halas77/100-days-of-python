import pandas as pd

df = pd.read_csv('day-71/592 salaries-by-college-major.csv')


cleared_df = df.dropna()

# print(cleared_df['Starting Median Salary'].loc[43])
# print(cleared_df['Undergraduate Major'].loc[43])
# print(cleared_df.loc[43])

# print(cleared_df['Mid-Career Median Salary'].idxmax())
# print(cleared_df['Undergraduate Major'].loc[cleared_df['Mid-Career Median Salary'].idxmax()])


# print(cleared_df['Undergraduate Major'].loc[cleared_df['Starting Median Salary'].idxmin()])


