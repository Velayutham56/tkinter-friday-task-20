import tkinter as tk
from tkinter import ttk, Frame, Listbox, Scrollbar
import re

# Email validation
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Register student
def register_student():
    name = entry_name.get()
    email = entry_email.get()
    course = combo_course.get()
    age = spin_age.get()

    if not name or not email or not is_valid_email(email):
        label_status.config(text="Please enter a valid name and email", fg="red")
        return

    summary = f"{name} ({age}) - {course}"
    listbox_students.insert(tk.END, summary)
    label_status.config(text="Student Registered!", fg="green")

# Main window
root = tk.Tk()
root.title("Student Registration App")

# Top frame for form inputs
frame_form = Frame(root, pady=10)
frame_form.pack()

# Name
tk.Label(frame_form, text="Name").pack()
entry_name = tk.Entry(frame_form)
entry_name.pack()

# Email
tk.Label(frame_form, text="Email").pack()
entry_email = tk.Entry(frame_form)
entry_email.pack()

# Course
tk.Label(frame_form, text="Course").pack()
combo_course = ttk.Combobox(frame_form, values=["Python", "Java", "Data Science", "Web Dev"])
combo_course.pack()
combo_course.set("Select Course")

# Age
tk.Label(frame_form, text="Age").pack()
spin_age = tk.Spinbox(frame_form, from_=5, to=100)
spin_age.pack()

# Submit Button
tk.Button(frame_form, text="Register", command=register_student).pack(pady=5)

# Status Label
label_status = tk.Label(frame_form, text="", fg="green")
label_status.pack()

# Bottom frame for listbox and scrollbar
frame_list = Frame(root, pady=10)
frame_list.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_list, text="Registered Students").pack()

# Scrollable listbox
scrollbar = Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_students = Listbox(frame_list, yscrollcommand=scrollbar.set, height=8)
listbox_students.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_students.yview)

root.mainloop()
