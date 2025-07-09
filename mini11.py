import tkinter as tk
from tkinter import ttk

def convert_temperature():
    temp = float(temp_spinbox.get())
    direction = direction_combo.get()
    
    if direction == "Celsius to Fahrenheit":
        converted = (temp * 9/5) + 32
        result_label.config(text=f"{converted:.2f} °F")
    elif direction == "Fahrenheit to Celsius":
        converted = (temp - 32) * 5/9
        result_label.config(text=f"{converted:.2f} °C")
    else:
        result_label.config(text="Choose a conversion")


root = tk.Tk()
root.title("Temperature Converter")


temp_spinbox = tk.Spinbox(root, from_=-100, to=100, width=10)
temp_spinbox.pack(pady=5)


direction_combo = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"])
direction_combo.pack(pady=5)
direction_combo.set("Choose Direction")


convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=5)


result_label = tk.Label(root, text="Result will appear here", font=("Helvetica", 12))
result_label.pack(pady=10)

root.mainloop()
