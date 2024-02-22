import pandas as pd

df = pd.read_csv('day-71/592 salaries-by-college-major.csv')


cleared_df = df.dropna()

# print(cleared_df['Starting Median Salary'].loc[43])
# print(cleared_df['Undergraduate Major'].loc[43])
# print(cleared_df.loc[43])

# print(cleared_df['Mid-Career Median Salary'].idxmax())
# print(cleared_df['Undergraduate Major'].loc[cleared_df['Mid-Career Median Salary'].idxmax()])


# print(cleared_df['Undergraduate Major'].loc[cleared_df['Starting Median Salary'].idxmin()])



# spread_col = cleared_df['Mid-Career 90th Percentile Salary'] - cleared_df['Mid-Career 10th Percentile Salary']
# cleared_df.insert(1, 'Spread', spread_col)

# low_risk = cleared_df.sort_values('Spread')


# print(low_risk['Undergraduate Major'][0])
# print(low_rist[['Undergraduate Major', 'Spread']].head())


# maxi = cleared_df['Spread'].idxmax()

# maxi = cleared_df['Undergraduate Major'].loc()


# print(maxi)

# print(cleared_df.groupby('Group').count())