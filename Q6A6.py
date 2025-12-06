import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Department': ['HR', 'IT', 'HR', 'Finance', 'IT'],
        'Salary': [60000, 75000, 62000, 80000, 78000]}
df = pd.DataFrame(data)
# Group by 'Department' and calculate the average 'Salary'
average_salary_by_department = df.groupby('Department')['Salary'].mean()
# Print the result
print("Average Salary by Department:")
print(average_salary_by_department)
