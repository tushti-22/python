import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

point = canvas.create_oval(10, 140, 20, 150, fill="red")
x_speed = 2

def move_point():
    canvas.move(point, x_speed, 0)
    canvas.after(20, move_point)

move_point()
root.mainloop()
