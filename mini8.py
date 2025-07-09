import tkinter as tk
from tkinter import messagebox
import os

tasks = []


def add_task():
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        tasks.append(task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def mark_done(event):
    index = listbox_tasks.curselection()
    if index:
        i = index[0]
        task_text = listbox_tasks.get(i)
        if not task_text.startswith("✓"):
            listbox_tasks.delete(i)
            listbox_tasks.insert(i, "✓ " + task_text)
            listbox_tasks.itemconfig(i, {'fg': 'green'})
            tasks[i] = "✓ " + tasks[i]

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for t in tasks:
            file.write(t + "\n")
    messagebox.showinfo("Saved", "Tasks saved to tasks.txt")

def load_tasks():
    if os.path.exists("tasks.txt"):
        listbox_tasks.delete(0, tk.END)
        tasks.clear()
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                task = line.strip()
                tasks.append(task)
                listbox_tasks.insert(tk.END, task)
                if task.startswith("✓"):
                    listbox_tasks.itemconfig(tk.END, {'fg': 'green'})


root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")


entry_task = tk.Entry(root, font=("Arial", 12))
entry_task.pack(pady=10, padx=10, fill=tk.X)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Add Task", command=add_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Save", command=save_tasks).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Load", command=load_tasks).pack(side=tk.LEFT, padx=5)


frame_list = tk.Frame(root)
frame_list.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks = tk.Listbox(frame_list, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox_tasks.yview)

listbox_tasks.bind("<Double-Button-1>", mark_done)

root.mainloop()
