import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = combo_op.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                label_result.config(text="Error: Division by zero", fg="red")
                return
            result = num1 / num2
        else:
            label_result.config(text="Select a valid operation", fg="red")
            return

        label_result.config(text=f"Result: {result}", fg="green")
    except ValueError:
        label_result.config(text="Invalid input. Use numbers only.", fg="red")

# Window setup
root = tk.Tk()
root.title("Simple Calculator")

# Labels & Entries
tk.Label(root, text="Number 1").grid(row=0, column=0, padx=5, pady=5)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Number 2").grid(row=1, column=0, padx=5, pady=5)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operation selection
tk.Label(root, text="Operation").grid(row=2, column=0, padx=5, pady=5)
combo_op = ttk.Combobox(root, values=["+", "-", "*", "/"], width=5)
combo_op.grid(row=2, column=1)
combo_op.set("+")

# Calculate Button
tk.Button(root, text="Calculate", command=calculate).grid(row=3, columnspan=2, pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=4, columnspan=2)

root.mainloop()
