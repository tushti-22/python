import pandas as pd
import io
# 5(a) Reading a CSV File
csv_data = """Name,Department,Salary
John,Sales,50000
Jane,Marketing,60000
Emily,HR,55000"""
# Read the CSV data into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))
# Print the contents of the DataFrame
print("Original DataFrame:")
print(df)
# 5(b) CSV Data Manipulation
# Filter the rows where the Salary is greater than 55000
filtered_df = df[df['Salary'] > 55000]
# Print only the Name and Department columns for the filtered rows
print("\nFiltered rows (Salary > 55000) - Name and Department columns:")
print(filtered_df[['Name', 'Department']])
