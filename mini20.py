import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Data storage
progress_data = {}

def update_progress():
    module = module_combo.get()
    level = int(understanding_spin.get())
    if module:
        progress_data[module] = level
        draw_progress_bar()
        if module not in completed_listbox.get(0, tk.END):
            completed_listbox.insert(tk.END, module)

def draw_progress_bar():
    canvas.delete("all")
    for i, (module, level) in enumerate(progress_data.items()):
        x = 20
        y = 30 + i * 30
        width = level * 20
        canvas.create_text(x, y, anchor="w", text=f"{module} ({level}/10)", font=("Helvetica", 10))
        canvas.create_rectangle(x + 150, y - 10, x + 150 + width, y + 10, fill="green")

def save_progress():
    with open("progress.json", "w") as file:
        json.dump(progress_data, file)
    messagebox.showinfo("Saved", "Progress saved successfully.")

def load_progress():
    if os.path.exists("progress.json"):
        with open("progress.json", "r") as file:
            loaded = json.load(file)
            progress_data.update(loaded)
            completed_listbox.delete(0, tk.END)
            for module in progress_data:
                completed_listbox.insert(tk.END, module)
            draw_progress_bar()

root = tk.Tk()
root.title("Tkinter Learning Dashboard")
root.geometry("500x400")

# Module selection
tk.Label(root, text="Select Module:", font=("Helvetica", 10)).place(x=20, y=20)
module_combo = ttk.Combobox(root, values=[
    "Canvas Basics", "Widgets Layout", "Event Binding", 
    "Animation Techniques", "Dynamic Resizing", "Drawing Tools"
], state="readonly")
module_combo.place(x=150, y=20, width=200)

# Understanding level
tk.Label(root, text="Understanding Level (1-10):", font=("Helvetica", 10)).place(x=20, y=60)
understanding_spin = tk.Spinbox(root, from_=1, to=10, width=5)
understanding_spin.place(x=230, y=60)

# Update button
update_btn = tk.Button(root, text="Update Progress", command=update_progress)
update_btn.place(x=180, y=100)

# Canvas for progress bars
canvas = tk.Canvas(root, width=460, height=150, bg="#f0f0f0")
canvas.place(x=20, y=140)

# Completed topics listbox
tk.Label(root, text="Completed Topics:", font=("Helvetica", 10)).place(x=20, y=300)
completed_listbox = tk.Listbox(root, height=5, width=30)
completed_listbox.place(x=150, y=300)

# Save/Load buttons
save_btn = tk.Button(root, text="Save", command=save_progress)
save_btn.place(x=400, y=300)

load_btn = tk.Button(root, text="Load", command=load_progress)
load_btn.place(x=400, y=330)

root.mainloop()
