import pandas as pd
s1 = pd.Series([100, 200, 300, 400, 500])
# 2(a) Creating a Series
print("2(a) S1 Series:")
print(s1)
print("\n")
# 2(b) Accessing Elements in a Series
second_element = s1.iloc[1]
fourth_element = s1.iloc[3]
# Print the accessed elements
print("2(b) Second and fourth elements:")
print(f"Second element: {second_element}")
print(f"Fourth element: {fourth_element}")
print("\n")
# 2(c) Series Operations
# Create a second Series S2
s2 = pd.Series([10, 20, 30, 40, 50])
# Perform element-wise addition between S1 and S2
addition_result = s1 + s2
# Print the result
print("2(c) Result of S1 + S2:")
print(addition_result)
