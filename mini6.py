import tkinter as tk
from tkinter import ttk

def draw_shape(event):
    x, y = event.x, event.y
    shape = combo_shape.get()
    color = combo_color.get()

    size = 100  # Fixed size for simplicity
    x0, y0 = x - size//2, y - size//2
    x1, y1 = x + size//2, y + size//2

    if shape == "Rectangle":
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
    elif shape == "Oval":
        canvas.create_oval(x0, y0, x1, y1, fill=color)


root = tk.Tk()
root.title("Canvas Drawing Tool")
root.geometry("500x400")


frame_controls = tk.Frame(root)
frame_controls.pack(pady=5)


tk.Label(frame_controls, text="Shape").pack(side=tk.LEFT, padx=5)
combo_shape = ttk.Combobox(frame_controls, values=["Rectangle", "Oval"], width=10)
combo_shape.pack(side=tk.LEFT)
combo_shape.set("Rectangle")


tk.Label(frame_controls, text="Color").pack(side=tk.LEFT, padx=5)
combo_color = ttk.Combobox(frame_controls, values=["red", "blue", "green", "yellow", "black"], width=10)
combo_color.pack(side=tk.LEFT)
combo_color.set("blue")


canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas.bind("<Button-1>", draw_shape)

root.mainloop()
