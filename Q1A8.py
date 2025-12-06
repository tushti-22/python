import math
class Point:
    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
    def distance_to(self,other):
        return math.hypot(self.x-other.x,self.y-other.y)
    def midpoint(self,other):
        return Point((self.x+other.x)/2,(self.y+other.y)/2)
    def to_tuple(self):
        return (self.x,self.y)
def line_equation(a,b):
    if a.x==b.x:
        return None, a.x
    m=(b.y-a.y)/(b.x-a.x)
    c=a.y-m*a.x
    return (m,c), None
def reflect_point_over_line(a,b,c):
    ax,ay=a.x,a.y
    bx,by=b.x,b.y
    px,py=c.x,c.y
    abx=bx-ax
    aby=by-ay
    ab_len=math.hypot(abx,aby)
    if ab_len==0:
        return Point(ax,ay)
    ux=abx/ab_len
    uy=aby/ab_len
    apx=px-ax
    apy=py-ay
    proj_len=apx*ux+apy*uy
    projx=ax+proj_len*ux
    projy=ay+proj_len*uy
    rx=2*projx-px
    ry=2*projy-py
    return Point(rx,ry)
a=Point(*map(float,input("Enter A (x y): ").split()))
b=Point(*map(float,input("Enter B (x y): ").split()))
c=Point(*map(float,input("Enter C (x y) for reflection: ").split()))
print("Distance A-B:", a.distance_to(b))
m_c, x_vert = line_equation(a,b)
if m_c is None:
    print("Line: x=", x_vert)
else:
    m,c_val = m_c
    print("Line: y = {}x + {}".format(m,c_val))
mid=a.midpoint(b)
print("Midpoint A-B:", mid.to_tuple())
ref=reflect_point_over_line(a,b,c)
print("Reflection of C over AB:", ref.to_tuple())
