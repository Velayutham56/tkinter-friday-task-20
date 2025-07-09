import tkinter as tk

def update_counts(event=None):
    text_content = text_box.get("1.0", tk.END)
    words = len(text_content.split())
    characters = len(text_content) - 1  # minus 1 to exclude the last newline
    count_label.config(text=f"Words: {words} | Characters: {characters}")

def reset():
    text_box.delete("1.0", tk.END)
    count_label.config(text="Words: 0 | Characters: 0")

root = tk.Tk()
root.title("Live Typing Tracker")

text_box = tk.Text(root, wrap=tk.WORD, font=("Helvetica", 12), width=50, height=10)
text_box.pack(padx=10, pady=(10, 0))
text_box.bind("<Key>", update_counts)

count_label = tk.Label(root, text="Words: 0 | Characters: 0", font=("Helvetica", 10))
count_label.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=(0, 10))

root.mainloop()
