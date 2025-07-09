import tkinter as tk
from tkinter import ttk

# Sample customer data
customers = {
    "Customer A": {"Name": "Aarthi", "Contact": "9876543210", "Address": "Chennai"},
    "Customer B": {"Name": "Balaji", "Contact": "8765432109", "Address": "Coimbatore"},
    "Customer C": {"Name": "Chetan", "Contact": "7654321098", "Address": "Madurai"}
}

def show_details(event):
    selected = combo.get()
    info = customers[selected]
    name_label.config(text=f"Name: {info['Name']}")
    contact_label.config(text=f"Contact: {info['Contact']}")
    address_label.config(text=f"Address: {info['Address']}")

    if disable_combo.get():  # Check if disabling is selected
        combo.config(state="disabled")

def reset():
    combo.set('')
    combo.config(state="readonly")
    name_label.config(text="Name: ")
    contact_label.config(text="Contact: ")
    address_label.config(text="Address: ")

root = tk.Tk()
root.title("Customer Info Viewer")

combo = ttk.Combobox(root, values=list(customers.keys()), state="readonly", font=("Helvetica", 12))
combo.set("Select Customer")
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", show_details)

name_label = tk.Label(root, text="Name: ", font=("Helvetica", 11))
name_label.pack()

contact_label = tk.Label(root, text="Contact: ", font=("Helvetica", 11))
contact_label.pack()

address_label = tk.Label(root, text="Address: ", font=("Helvetica", 11))
address_label.pack()

disable_combo = tk.BooleanVar()
disable_check = tk.Checkbutton(root, text="Disable after selection", variable=disable_combo)
disable_check.pack(pady=5)

reset_btn = tk.Button(root, text="Reset", command=reset)
reset_btn.pack(pady=10)

root.mainloop()
