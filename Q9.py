import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

students = ["Arin","Aditya","Chirag","Gurleen","Kunal"]
marks = np.array([[85,78,92,88],[79,82,74,90],[90,85,89,92],[66,75,80,78],[70,68,75,85]])
df = pd.DataFrame(marks, index=students, columns=["Math","Physics","Chemistry","English"])

df.plot(kind='bar')
plt.show()
