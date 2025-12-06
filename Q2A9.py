import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# small circle to represent point
canvas.create_oval(98, 98, 102, 102, fill="black")

root.mainloop()
