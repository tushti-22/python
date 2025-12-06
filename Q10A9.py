import tkinter as tk

root = tk.Tk()
root.title("Robot Path Drawer")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Robot
x, y = 300, 200
robot = canvas.create_oval(x-10, y-10, x+10, y+10, fill="blue")

path_lines = []

def move(dx, dy):
    global x, y

    new_x = x + dx
    new_y = y + dy

    # Draw path line
    line = canvas.create_line(x, y, new_x, new_y, fill="black")
    path_lines.append(line)

    # Move robot
    canvas.move(robot, dx, dy)

    x, y = new_x, new_y

def key_press(event):
    if event.keysym == "Up":
        move(0, -5)
    elif event.keysym == "Down":
        move(0, 5)
    elif event.keysym == "Left":
        move(-5, 5)
    elif event.keysym == "Right":
        move(5, 0)

root.bind("<KeyPress>", key_press)

def reset_path():
    for line in path_lines:
        canvas.delete(line)
    path_lines.clear()

tk.Button(root, text="RESET", command=reset_path, font=("Arial", 14)).pack(pady=10)

root.mainloop()
