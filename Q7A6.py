import pandas as pd
# Create the first DataFrame
df1 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Department': ['Sales', 'Marketing', 'HR']
})
# Create the second DataFrame
df2 = pd.DataFrame({
    'Name': ['John', 'Jane', 'Emily'],
    'Experience (Years)': [5, 7, 3]
})
# Merge the two DataFrames on the 'Name' column
merged_df = pd.merge(df1, df2, on='Name')
# Print the merged DataFrame
print(merged_df)
