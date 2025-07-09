import tkinter as tk

def save_feedback():
    name = name_entry.get()
    email = email_entry.get()
    comments = comment_box.get("1.0", tk.END).strip()
    rating = rating_spinbox.get()

    if name and email and comments:
        entry = f"{name} ({email}) - Rating: {rating}\nComment: {comments}"
        feedback_listbox.insert(tk.END, entry)
        thank_you_label.config(text="Thanks for your feedback!")
        
        # Clear fields
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        comment_box.delete("1.0", tk.END)
        rating_spinbox.delete(0, tk.END)
        rating_spinbox.insert(0, "5")
    else:
        thank_you_label.config(text="Please fill all fields before submitting.")

# Main window
root = tk.Tk()
root.title("Feedback Form")

# Name and Email
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)
name_entry.insert(0, "Name")

email_entry = tk.Entry(root, width=30)
email_entry.pack(pady=5)
email_entry.insert(0, "Email")

# Comments
comment_box = tk.Text(root, width=40, height=5)
comment_box.pack(pady=5)

# Rating
rating_spinbox = tk.Spinbox(root, from_=1, to=10, width=5)
rating_spinbox.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit Feedback", command=save_feedback)
submit_button.pack(pady=5)

# Thank-you message
thank_you_label = tk.Label(root, text="", fg="green")
thank_you_label.pack(pady=5)

# Feedback Listbox with Scrollbar
frame = tk.Frame(root)
frame.pack(pady=10)

feedback_listbox = tk.Listbox(frame, width=60, height=10)
feedback_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=feedback_listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

feedback_listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()
