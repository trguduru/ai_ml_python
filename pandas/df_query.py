# exmaples using dataframe query method
import pandas as pd
df = pd.read_csv('/Users/tguduru/AI-ML-UC-Berkley-Course/DataSets_starter/celebrity-heights.csv')
print(df.head(2))

# query usage
print(df.query('gender == "M"'))

# query with and
print(df.query('gender == "M" and feet == 7'))

#query with or
print(df.query('gender == "M" or feet == 7'))

print(df.isin([7,8]))
