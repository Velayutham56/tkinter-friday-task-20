import tkinter as tk
from tkinter import ttk

def add_shift():
    name = name_entry.get()
    shift = shift_combo.get()
    hours = hours_spin.get()
    if name and shift and hours:
        entry = f"{name} | Shift: {shift} | Hours: {hours}"
        shift_list.insert(tk.END, entry)
        name_entry.delete(0, tk.END)
        shift_combo.set("")
        hours_spin.delete(0, tk.END)
        hours_spin.insert(0, "1")

root = tk.Tk()
root.title("Employee Shift Scheduler")

main_frame = tk.Frame(root)
main_frame.grid(padx=10, pady=10)

# Employee Name
tk.Label(main_frame, text="Employee Name:", font=("Helvetica", 11)).grid(row=0, column=0, sticky="e")
name_entry = tk.Entry(main_frame, font=("Helvetica", 11))
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Shift Type
tk.Label(main_frame, text="Shift Type:", font=("Helvetica", 11)).grid(row=1, column=0, sticky="e")
shift_combo = ttk.Combobox(main_frame, values=["Morning", "Afternoon", "Night"], state="readonly", font=("Helvetica", 11))
shift_combo.grid(row=1, column=1, padx=5, pady=5)

# Working Hours
tk.Label(main_frame, text="Hours:", font=("Helvetica", 11)).grid(row=2, column=0, sticky="e")
hours_spin = tk.Spinbox(main_frame, from_=1, to=12, font=("Helvetica", 11), width=5)
hours_spin.grid(row=2, column=1, padx=5, pady=5)

# Add Button
add_button = tk.Button(main_frame, text="Add Shift", command=add_shift, font=("Helvetica", 11))
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Shift List
list_frame = tk.Frame(root)
list_frame.grid(row=1, column=0, padx=10, pady=(0, 10))

shift_list = tk.Listbox(list_frame, width=50, height=10, font=("Helvetica", 10))
shift_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

shift_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=shift_list.yview)

root.mainloop()
