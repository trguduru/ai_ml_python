# examples explain how to use DataFrames by reading from external source like excel,csv, url based etc ...
import pandas as pd
df = pd.read_csv("/Users/tguduru/AI-ML-UC-Berkley-Course/DataSets_starter/celebrity-heights.csv")
print(df)



print(df.head(), df.tail())
