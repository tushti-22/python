import scipy as sp
import pandas as pd
print(sp.__version__)
print(pd.__version__)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("\nCreated DataFrame:")
print(df)
