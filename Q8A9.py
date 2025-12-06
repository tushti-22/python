import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=300, bg="white")
canvas.pack()

x, y = 50, 200
target_x = 450
velocity = 2

robot = canvas.create_oval(x-10, y-10, x+10, y+10, fill="green")

def move_robot():
    global x
    if x < target_x:
        x += velocity
        canvas.coords(robot, x-10, y-10, x+10, y+10)
        canvas.after(20, move_robot)

move_robot()
root.mainloop()
