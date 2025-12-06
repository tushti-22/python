import numpy as np
a1,b1,c1=map(float,input("Enter a1 b1 c1 for a1*x + b1*y = c1: ").split())
a2,b2,c2=map(float,input("Enter a2 b2 c2 for a2*x + b2*y = c2: ").split())
det=a1*b2-a2*b1
if abs(det) > 1e-12:
    x=(c1*b2-c2*b1)/det
    y=(a1*c2-a2*c1)/det
    print("Intersection point (x,y):", (x,y))
else:
    print("Lines are parallel or coincident.")
