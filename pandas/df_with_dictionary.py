# example usages of pandas dataframe APIs using dictionary
import pandas as pd

lords = {"name": ["Ram", "Bheem", "Krishna", "Arjun", "Shiva"],
         "age": [10, 11, 10, 11, 12],
         "grades": ["A*", "A++", "A++", "A", "A*"],
         "course": ["Arrow", "Gadha", "Chakra", "Arrow", "Trishula"]}

print("Lords dictionary", lords)

# create a dataframe using pandas library with dictionary
df = pd.DataFrame(lords)

print("Data Frame: ")
print(df)

print(df.columns)

# basic DataFrame APIs usage

print("Shape: ", df.shape)  # shows the columns and rows of the data frame as a tuple
print("Info: ")
print(df.info())

print(df.head(2))  # returns the top n rows, default 5
print(df.tail(2))  # returns the bottom n rows, default 5

print("Size", df.size)  # returns the total number of elements, its rows * columns

print("Column Values (name,etc....): ")
print(df['name'])
print(df[['name', 'age']])  # should be a list of columns if there is more than one

print("All Column names : ", df.columns)

print(df.iloc[0])  # returns the row of integer location starts with '0'

# returns the rows at index 0,1 and only with columns name and age,its range for columns
print(df.loc[[0, 1], ['name', 'age']])

# indexes, labelling the indexes
# the difference between iloc and loc is loc returns by index labels which you can see below

df_indexed = df.set_index('age')  # this will remove the age column and set that as index
print(df_indexed.loc[10])  # returns the rows using the index

df_indexed = df.set_index('name')
print("Row Values (Ram)")
print(df_indexed.loc['Ram'])

# reset index labels
print(df_indexed.reset_index())

# the sort_index method will sort the data frame based on the index labels
print(df_indexed.sort_index())
print(df_indexed.sort_index(ascending=False))

# Filtering DataFrame

filtered_series = df_indexed['grades'] == "A*"  # returns a series of filtered 'A*' grade lords

print(df_indexed[filtered_series])  # return the filtered dataframe
print(df_indexed.loc[filtered_series, 'course'])  # returns the same like above but can add additional columns

# Updating Rows / Columns

# modifying column labels/names
modified_df = [x.upper() for x in df.columns]
print(modified_df)  # you see in upper case columns
# modifying column names will be useful only when column names in the source data has spaces
modified_df = df.columns.str.replace('', "_")
print(modified_df)

# rename columns
m_df = df.rename(columns={'name': 'l_name','age': 'l_age', 'grade': 'l_grade', 'course': 'l_course'})
print("Renamed columns dataframe")
print(m_df)

# update a value in a row
# updating Ram age to 11
m_df.loc[0, 'l_age'] = 11  # you can set multiple column values as well using list
print(m_df)

m_df.at[0, 'l_age'] = 10   # can use .at as well if only single value needs change
print(m_df)

# apply values to a series
print(m_df['l_name'].apply(lambda x: x.upper()))

# add/remove rows and columns
df['full_name'] = m_df['l_name']  # if the column exists it will replace else add the column to the dataframe
print(df)

# remove a column
df = df.drop(columns='full_name')
print(df)

# add a new row , see https://pandas.pydata.org/docs/user_guide/merging.html#appending-rows-to-a-dataframe
s = pd.Series(["Karna"], index=["name"])
df = pd.concat([df, s.to_frame().T], ignore_index=True)
print(df)

# merge data frames , see https://pandas.pydata.org/docs/user_guide/merging.html#concatenating-objects
kids = {"name": ["Lava", "Gatotkacha", "Pradyumna", "Abhimanyu", "Vinayaka"],
         "age": [10, 11, 10, 11, 12],
         "grades": ["A*", "A++", "A++", "A", "A*"],
         "course": ["Arrow", "Gadha", "Chakra", "Chatram", "Trishula"]}

df2 = pd.DataFrame(kids)
final_df = pd.concat([df, df2], ignore_index=True)
print(final_df)

# remove a row
print(final_df.drop(index=10))  # remove the row at index 10

print(df.iloc[-1, ['name']])
