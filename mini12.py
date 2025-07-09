import tkinter as tk

def show_details(event):
    selection = product_listbox.curselection()
    if selection:
        product = product_listbox.get(selection[0])
        detail_label.config(text=f"Selected Product:\n{product}")

def add_product():
    new_product = product_entry.get()
    if new_product:
        product_listbox.insert(tk.END, new_product)
        product_entry.delete(0, tk.END)

def delete_product():
    selection = product_listbox.curselection()
    if selection:
        product_listbox.delete(selection[0])
        detail_label.config(text="")

# Root window
root = tk.Tk()
root.title("Product List Manager")

# Main frame
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# Listbox with Scrollbar
list_frame = tk.Frame(main_frame)
list_frame.pack(side=tk.LEFT)

product_listbox = tk.Listbox(list_frame, width=30, height=15)
product_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=product_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
product_listbox.config(yscrollcommand=scrollbar.set)

# Populate with 50+ dummy products
for i in range(1, 55):
    product_listbox.insert(tk.END, f"Product {i}")

product_listbox.bind("<<ListboxSelect>>", show_details)

# Right-side control panel
control_frame = tk.Frame(main_frame)
control_frame.pack(side=tk.RIGHT, padx=10)

product_entry = tk.Entry(control_frame)
product_entry.pack(pady=5)

add_button = tk.Button(control_frame, text="Add Product", command=add_product)
add_button.pack(pady=5)

delete_button = tk.Button(control_frame, text="Delete Product", command=delete_product)
delete_button.pack(pady=5)

detail_label = tk.Label(control_frame, text="Selected Product:", width=30, height=4, wraplength=200, bg="#eef")
detail_label.pack(pady=10)

root.mainloop()
