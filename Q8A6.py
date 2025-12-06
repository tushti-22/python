import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Experience (Years)': [5, 10, 3, 8],
        'Salary': [60000, 80000, 45000, 75000]}
df = pd.DataFrame(data)
# Sort the DataFrame by 'Experience (Years)' in descending order
sorted_df = df.sort_values(by='Experience (Years)', ascending=False)
# Print the sorted DataFrame
print(sorted_df)
