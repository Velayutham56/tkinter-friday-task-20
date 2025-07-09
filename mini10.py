import tkinter as tk

def generate_card():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    
    canvas.delete("all")  
    canvas.create_rectangle(50, 50, 350, 250, fill="#ddeeff", outline="#336699", width=2)
    canvas.create_text(200, 80, text=f"Name: {name}", font=("Helvetica", 14), fill="black")
    canvas.create_text(200, 120, text=f"Age: {age}", font=("Helvetica", 14), fill="black")
    canvas.create_text(200, 160, text=f"Email: {email}", font=("Helvetica", 14), fill="black")
    canvas.create_text(200, 210, text="User Profile Card", font=("Helvetica", 12, "italic"), fill="#555")


root = tk.Tk()
root.title("User Profile Card Generator")


input_frame = tk.Frame(root)
input_frame.pack(pady=10)


name_entry = tk.Entry(input_frame)
name_entry.pack()
name_entry.insert(0, "Enter name")

age_entry = tk.Entry(input_frame)
age_entry.pack()
age_entry.insert(0, "Enter age")

email_entry = tk.Entry(input_frame)
email_entry.pack()
email_entry.insert(0, "Enter email")


generate_button = tk.Button(input_frame, text="Generate Card", command=generate_card)
generate_button.pack(pady=5)


canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

root.mainloop()
