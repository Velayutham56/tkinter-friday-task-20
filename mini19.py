import tkinter as tk
from tkinter import filedialog

def apply_settings():
    title = title_entry.get()
    width = width_entry.get()
    height = height_entry.get()
    
    if title:
        root.title(title)
    
    if width.isdigit() and height.isdigit():
        root.geometry(f"{width}x{height}")

    icon_path = icon_entry.get()
    if icon_path:
        try:
            root.iconbitmap(icon_path)
        except:
            icon_status.config(text="Invalid .ico file", fg="red")
        else:
            icon_status.config(text="Icon applied", fg="green")

def browse_icon():
    file_path = filedialog.askopenfilename(title="Choose Icon", filetypes=[("ICO files", "*.ico")])
    icon_entry.delete(0, tk.END)
    icon_entry.insert(0, file_path)

root = tk.Tk()
root.title("Window Configurator")
root.geometry("400x250")

# Title Entry
tk.Label(root, text="Window Title:", font=("Helvetica", 10)).place(x=20, y=20)
title_entry = tk.Entry(root, font=("Helvetica", 10))
title_entry.place(x=130, y=20, width=200)

# Width Entry
tk.Label(root, text="Width:", font=("Helvetica", 10)).place(x=20, y=60)
width_entry = tk.Entry(root, font=("Helvetica", 10))
width_entry.place(x=130, y=60, width=80)

# Height Entry
tk.Label(root, text="Height:", font=("Helvetica", 10)).place(x=220, y=60)
height_entry = tk.Entry(root, font=("Helvetica", 10))
height_entry.place(x=280, y=60, width=80)

# Icon Entry
tk.Label(root, text="Icon File (.ico):", font=("Helvetica", 10)).place(x=20, y=100)
icon_entry = tk.Entry(root, font=("Helvetica", 10))
icon_entry.place(x=130, y=100, width=170)
browse_button = tk.Button(root, text="Browse", command=browse_icon)
browse_button.place(x=310, y=98)

# Status Label for icon feedback
icon_status = tk.Label(root, text="", font=("Helvetica", 9))
icon_status.place(x=130, y=130)

# Apply Button
apply_btn = tk.Button(root, text="Apply", command=apply_settings, font=("Helvetica", 11))
apply_btn.place(x=160, y=170)

root.mainloop()
