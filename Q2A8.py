import math
import numpy as np
def read_vec(name):
    return np.array(list(map(float,input(f"Enter vector {name} components (x y): ").split())))
A=read_vec('A')
B=read_vec('B')
C=read_vec('C')
R=A+B+C
def mag(v):
    return math.hypot(v[0],v[1])
def dot(u,v):
    return float(np.dot(u,v))
def angle_deg(u,v):
    du=mag(u); dv=mag(v)
    if du==0 or dv==0:
        return None
    cosv=dot(u,v)/(du*dv)
    cosv=max(-1,min(1,cosv))
    return math.degrees(math.acos(cosv))
def proj(u,v):
    dv2=dot(v,v)
    if dv2==0:
        return np.array([0.0,0.0])
    return (dot(u,v)/dv2)*v
print("Resultant R:", tuple(R))
print("Magnitude |A|:", mag(A))
print("Magnitude |B|:", mag(B))
print("Magnitude |C|:", mag(C))
print("Dot A.B:", dot(A,B))
print("Dot A.C:", dot(A,C))
print("Dot B.C:", dot(B,C))
print("Angle A-B (deg):", angle_deg(A,B))
print("Angle A-C (deg):", angle_deg(A,C))
print("Angle B-C (deg):", angle_deg(B,C))
print("Projection of A onto B:", tuple(proj(A,B)))
