import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

points = [20, 50, 100, 120, 180, 90, 250, 150]
canvas.create_line(points, fill="blue", width=3)

root.mainloop()
