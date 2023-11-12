import pandas as pd

# # Creating a sample DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'Age': [25, 30, 35, 28],
#         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

# df = pd.DataFrame(data)
# df.index = ['a', 'b', 'c', 'd']  # Assigning custom index labels

# print(df.loc[(df["Age"] == 25) ,"Name"])
# # Using .loc[] for label-based indexing
# print("Using .loc[]:")
# print(df.loc['b', 'Name'])  # Selecting the 'Name' column for row 'b'
# print(df.loc[['b', 'c'], ['Name', 'City']])  # Selecting specific rows and columns

# # Using .iloc[] for integer-location based indexing
# print("\nUsing .iloc[]:")
# print(df.iloc[2, 1])  # Selecting the value at row 2, column 1
# print(df.iloc[1:3, 0:2])  # Selecting a range of rows and columns

# # Using .at[] for fast label-based scalar accessor
# print("\nUsing .at[]:")
# print(df.at['c', 'Age'])  # Selecting the age at row 'c'

# # Using .iat[] for fast integer-location scalar accessor
# print("\nUsing .iat[]:")
# print(df.iat[0, 2])  # Selecting the value at row 0, column 2

# # Using .query() for DataFrame query
# print("\nUsing .query():")
# print(df.query('Age > 30'))  # Selecting rows where Age is greater than 30

# # Using Boolean Indexing
# print("\nUsing Boolean Indexing:")
# print(df[df['City'] == 'San Francisco'])  # Selecting rows where City is 'San Francisco'

