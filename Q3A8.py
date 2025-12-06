import math
import numpy as np
Sx,Sy=map(float,input("Enter S (x y): ").split())
Ex,Ey=map(float,input("Enter E (x y): ").split())
Px,Py=map(float,input("Enter P (x y): ").split())
S=np.array([Sx,Sy]); E=np.array([Ex,Ey]); P=np.array([Px,Py])
SE=E-S
length_segment=math.hypot(SE[0],SE[1])
print("Length of segment SE:", length_segment)
se_len2=SE.dot(SE)
if se_len2==0:
    closest=S
else:
    t=((P-S).dot(SE))/se_len2
    t_clamped=max(0,min(1,t))
    closest=S+t_clamped*SE
print("Closest point on SE to P:", (float(closest[0]), float(closest[1])))
dist_point_segment=math.hypot(P[0]-closest[0],P[1]-closest[1])
print("Distance from P to segment SE:", dist_point_segment)
