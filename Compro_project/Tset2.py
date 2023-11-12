import pandas as pd

# Creating a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
df.index = ['a', 'b', 'c', 'd']  # Assigning custom index labels

print(df.loc[(df["Age"] == 25) ,"Name"])
# Using .loc[] for label-based indexing
print("Using .loc[]:")
print(df.loc['b', 'Name'])  # Selecting the 'Name' column for row 'b'
print(df.loc[['b', 'c'], ['Name', 'City']])  # Selecting specific rows and columns

# Using .iloc[] for integer-location based indexing
print("\nUsing .iloc[]:")
print(df.iloc[2, 1])  # Selecting the value at row 2, column 1
print(df.iloc[1:3, 0:2])  # Selecting a range of rows and columns

# Using .at[] for fast label-based scalar accessor
print("\nUsing .at[]:")
print(df.at['c', 'Age'])  # Selecting the age at row 'c'

# Using .iat[] for fast integer-location scalar accessor
print("\nUsing .iat[]:")
print(df.iat[0, 2])  # Selecting the value at row 0, column 2

# Using .query() for DataFrame query
print("\nUsing .query():")
print(df.query('Age > 30'))  # Selecting rows where Age is greater than 30

# Using Boolean Indexing
print("\nUsing Boolean Indexing:")
print(df[df['City'] == 'San Francisco'])  # Selecting rows where City is 'San Francisco'


# Get input from the user
# user_input = input("Enter data separated by a forward slash (/): ")

# # Split the input using the forward slash
# data_list = user_input.split('/')

# # Display the result
# print("Split data:", data_list)
# print("\\n")




# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits 
#     password = ''.join(random.choice(characters) for i in range(length))
#     return password

# # Example usage with a default length of 12 characters
# password = generate_password()
# print(password)

# password = generate_password()

# print(password)


# hey = int(input("hey:"))
# print(len(str(hey)))
# while hey != "yo":
#         print("in the loop")
#         hey = input("hey:")


