import tkinter as tk
from tkinter import ttk

def draw_circle(event):
    color = color_combo.get()
    x, y = event.x, event.y
    canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="black")
    coord_label.config(text=f"Circle at ({x}, {y})")

def draw_square(event):
    color = color_combo.get()
    x, y = event.x, event.y
    canvas.create_rectangle(x-20, y-20, x+20, y+20, fill=color, outline="black")
    coord_label.config(text=f"Square at ({x}, {y})")

# Root window
root = tk.Tk()
root.title("Shape Drawer with Coordinates")

# Canvas setup
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(padx=10, pady=10)

# Bind mouse events
canvas.bind("<Button-1>", draw_circle)
canvas.bind("<Button-3>", draw_square)

# Color selector
color_combo = ttk.Combobox(root, values=["red", "blue", "green", "yellow", "purple"])
color_combo.set("red")
color_combo.pack(pady=5)

# Coordinate display
coord_label = tk.Label(root, text="Click on canvas to draw a shape", font=("Helvetica", 12))
coord_label.pack(pady=5)

root.mainloop()
