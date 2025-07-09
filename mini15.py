import tkinter as tk
from tkinter import ttk

def issue_book():
    name = name_entry.get()
    book = book_combo.get()
    date = date_spinbox.get()
    
    if name and book:
        record = f"{name} issued '{book}' on Day {date}"
        record_listbox.insert(tk.END, record)
        status_label.config(text="Book issued successfully!", fg="green")
        name_entry.delete(0, tk.END)
    else:
        status_label.config(text="Please fill in all details.", fg="red")

# Root setup
root = tk.Tk()
root.title("Library Book Issue System")

# Widgets
tk.Label(root, text="User Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Book Title").grid(row=1, column=0, padx=5, pady=5)
book_combo = ttk.Combobox(root, values=["Python Basics", "AI Essentials", "Tkinter Guide", "Data Science 101"])
book_combo.grid(row=1, column=1, padx=5, pady=5)
book_combo.set("Select Book")

tk.Label(root, text="Issue Date").grid(row=2, column=0, padx=5, pady=5)
date_spinbox = tk.Spinbox(root, from_=1, to=31, width=5)
date_spinbox.grid(row=2, column=1, padx=5, pady=5)

issue_button = tk.Button(root, text="Issue Book", command=issue_book)
issue_button.grid(row=3, column=0, columnspan=2, pady=5)

status_label = tk.Label(root, text="", font=("Helvetica", 10))
status_label.grid(row=4, column=0, columnspan=2)

# Record list with scrollbar
tk.Label(root, text="Issued Records").grid(row=5, column=0, columnspan=2, pady=(10,0))

frame = tk.Frame(root)
frame.grid(row=6, column=0, columnspan=2)

record_listbox = tk.Listbox(frame, width=50, height=10)
record_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, command=record_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
record_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
