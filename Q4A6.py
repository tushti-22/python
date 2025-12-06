import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 22],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Sydney']}
df = pd.DataFrame(data)
# Filter the DataFrame where Age is greater than 28
filtered_df = df[df['Age'] > 28]
print("Filtered DataFrame (Age > 28):")
print(filtered_df)
