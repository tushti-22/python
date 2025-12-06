import numpy as np
positions = np.array([[0,0], [2,3], [4,7], [7,10], [10,15]])
# Euclidean distance
distance = np.linalg.norm(positions[-1] - positions[0])
print("Euclidean distance (first to last):", distance)
