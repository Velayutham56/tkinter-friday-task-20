import tkinter as tk

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "1234"

def validate_login():
    user = entry_user.get()
    pwd = entry_pass.get()

    if user == USERNAME and pwd == PASSWORD:
        show_welcome(user)
        login_window.destroy()
    else:
        label_status.config(text="Invalid credentials!", fg="red")

def show_welcome(username):
    welcome_window = tk.Tk()
    welcome_window.title("Welcome Screen")
    welcome_window.geometry("300x150")

    tk.Label(welcome_window, text=f"Welcome, {username}!", font=("Helvetica", 14)).pack(pady=50)
    welcome_window.mainloop()


login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")


tk.Label(login_window, text="Username").place(x=60, y=40)
entry_user = tk.Entry(login_window)
entry_user.place(x=140, y=40)


tk.Label(login_window, text="Password").place(x=60, y=80)
entry_pass = tk.Entry(login_window, show="*")
entry_pass.place(x=140, y=80)


tk.Button(login_window, text="Login", command=validate_login).place(x=120, y=120)


label_status = tk.Label(login_window, text="", fg="green")
label_status.place(x=90, y=160)

login_window.mainloop()
