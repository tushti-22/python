import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=350, bg="white")
canvas.pack()

r = 15
ball = canvas.create_oval(200-r, 150-r, 200+r, 150+r, fill="red")

dx, dy = 3, 3

def animate():
    global dx, dy
    canvas.move(ball, dx, dy)
    x1, y1, x2, y2 = canvas.coords(ball)

    if x1 <= 0 or x2 >= 500:
        dx = -dx
    if y1 <= 0 or y2 >= 350:
        dy = -dy

    canvas.after(20, animate)

animate()
root.mainloop()
