import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Spinbox, Text
import re


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def submit():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    age = spin_age.get()
    about = text_about.get("1.0", tk.END).strip()

    if not is_valid_email(email):
        label_result.config(text="Invalid Email", fg="red")
        return

    result = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAge: {age}\nAbout: {about}"
    label_result.config(text=result, fg="green")


root = tk.Tk()
root.title("Personal Information Form")


frame_top = Frame(root, padx=10, pady=10)
frame_top.grid(row=0, column=0)

frame_bottom = Frame(root, padx=10, pady=10)
frame_bottom.grid(row=1, column=0)


Label(frame_top, text="Name").grid(row=0, column=0, sticky="w")
entry_name = Entry(frame_top)
entry_name.grid(row=0, column=1)


Label(frame_top, text="Email").grid(row=1, column=0, sticky="w")
entry_email = Entry(frame_top)
entry_email.grid(row=1, column=1)


Label(frame_top, text="Phone").grid(row=2, column=0, sticky="w")
entry_phone = Entry(frame_top)
entry_phone.grid(row=2, column=1)


Label(frame_top, text="Age").grid(row=3, column=0, sticky="w")
spin_age = Spinbox(frame_top, from_=1, to=120)
spin_age.grid(row=3, column=1)


Label(frame_bottom, text="About You").grid(row=0, column=0, sticky="nw")
text_about = Text(frame_bottom, height=5, width=30)
text_about.grid(row=0, column=1)


Button(root, text="Submit", command=submit).grid(row=2, column=0)


label_result = Label(root, text="", fg="green", justify="left")
label_result.grid(row=3, column=0, pady=10)

root.mainloop()
