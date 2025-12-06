import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
np.random.seed(0)
sales = np.random.randint(200,1000,size=(12,4))
products = ["P1","P2","P3","P4"]
df = pd.DataFrame(sales, index=months, columns=products)
df['Total'] = df.sum(axis=1)

print(df)
print("Best month:", df['Total'].idxmax())
print("Worst month:", df['Total'].idxmin())

df['Total'].plot(marker='o')
plt.show()
