import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'London', 'Paris']}
df = pd.DataFrame(data)
# 3(a) DataFrame Column Access
print("3(a) 'Name' and 'City' columns:")
print(df[['Name', 'City']])
# 3(b) Adding a New Column
df['Salary'] = [50000, 60000, 70000]
print("\n3(b) DataFrame after adding 'Salary' column:")
print(df)
# 3(c) Basic Statistics on DataFrames
average_age = df['Age'].mean()
total_salary = df['Salary'].sum()
print(f"\n3(c) Basic Statistics:")
print(f"Average Age: {average_age}")
print(f"Total Sum of Salary: {total_salary}")
