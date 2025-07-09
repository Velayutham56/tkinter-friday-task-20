import tkinter as tk

# Preset content for loading
PRESET_TEXT = """Welcome to your mini Notepad!
Feel free to edit this content."""

# Functions
def save_text():
    content = text_area.get("1.0", tk.END).strip()
    print("Saved Content:\n", content)
    update_word_count()

def clear_text():
    text_area.delete("1.0", tk.END)
    update_word_count()

def load_preset():
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, PRESET_TEXT)
    update_word_count()

def update_word_count():
    content = text_area.get("1.0", tk.END).strip()
    words = content.split()
    label_word_count.config(text=f"Word Count: {len(words)}")

# Main window
root = tk.Tk()
root.title("Mini Notepad")
root.geometry("400x350")

# Text area
text_area = tk.Text(root, wrap="word", font=("Arial", 12))
text_area.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

# Buttons frame
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=5)

tk.Button(frame_buttons, text="Save", command=save_text).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Clear", command=clear_text).pack(side=tk.LEFT, padx=5)
tk.Button(frame_buttons, text="Load Preset", command=load_preset).pack(side=tk.LEFT, padx=5)

# Word count label
label_word_count = tk.Label(root, text="Word Count: 0", font=("Arial", 10))
label_word_count.pack(pady=5)

# Bind text changes to update word count
def on_text_change(event):
    update_word_count()
    return "break"  # avoid inserting unwanted characters from the event

text_area.bind("<KeyRelease>", on_text_change)

root.mainloop()
