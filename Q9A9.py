import tkinter as tk
import math

root = tk.Tk()
root.title("Four-Bar Mechanism")

canvas = tk.Canvas(root, width=700, height=500, bg="white")
canvas.pack()

# Given
A = (150, 300)
D = (400, 300)

L2 = 120   # crank
L3 = 150   # coupler
L4 = 130   # rocker
theta = math.radians(30)

# Compute B (end of crank)
Bx = A[0] + L2 * math.cos(theta)
By = A[1] - L2 * math.sin(theta)
B = (Bx, By)

# Compute C (intersection of two circles)
# Circle 1: center B radius L3
# Circle 2: center D radius L4

def circle_intersection(x0,y0,r0, x1,y1,r1):
    dx = x1 - x0
    dy = y1 - y0
    d = math.hypot(dx, dy)
    a = (r0*r0 - r1*r1 + d*d) / (2*d)
    h = math.sqrt(abs(r0*r0 - a*a))

    xm = x0 + a * dx/d
    ym = y0 + a * dy/d

    xs1 = xm + h * dy/d
    ys1 = ym - h * dx/d

    xs2 = xm - h * dy/d
    ys2 = ym + h * dx/d

    return (xs1, ys1), (xs2, ys2)

C1, C2 = circle_intersection(B[0], B[1], L3, D[0], D[1], L4)

C = C1   # choose first intersection

# Draw joints
r = 5
def draw_point(P, color):
    canvas.create_oval(P[0]-r, P[1]-r, P[0]+r, P[1]+r, fill=color)

draw_point(A, "red")
draw_point(B, "blue")
draw_point(C, "green")
draw_point(D, "black")

# Draw links (different colors)
canvas.create_line(A[0], A[1], B[0], B[1], width=4, fill="blue")    # crank
canvas.create_line(B[0], B[1], C[0], C[1], width=4, fill="green")  # coupler
canvas.create_line(C[0], C[1], D[0], D[1], width=4, fill="orange") # rocker
canvas.create_line(A[0], A[1], D[0], D[1], width=4, fill="red")    # ground

root.mainloop()
