import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.create_rectangle(100, 100, 250, 180, fill="gray")

canvas.create_oval(110, 180, 150, 220, fill="black")
canvas.create_oval(200, 180, 240, 220, fill="black")

root.mainloop()
