import tkinter as tk


x_pos = 0
y_pos = 100
dx = 5
animation_running = False

def move_object():
    global x_pos, animation_running
    if animation_running:
        x_pos += dx
        canvas.coords(rect, x_pos, y_pos, x_pos + 50, y_pos + 30)
        label_coords.config(text=f"X: {x_pos}, Y: {y_pos}")
        root.after(int(speed_spin.get()), move_object)

def start_animation():
    global animation_running
    if not animation_running:
        animation_running = True
        move_object()

def stop_animation():
    global animation_running
    animation_running = False


root = tk.Tk()
root.title("Animated Rectangle")
root.geometry("500x300")


canvas = tk.Canvas(root, width=480, height=200, bg="white")
canvas.pack(pady=10)
rect = canvas.create_rectangle(x_pos, y_pos, x_pos + 50, y_pos + 30, fill="blue")


frame_controls = tk.Frame(root)
frame_controls.pack(pady=5)


tk.Label(frame_controls, text="Speed (ms):").pack(side=tk.LEFT, padx=5)
speed_spin = tk.Spinbox(frame_controls, from_=1, to=1000, width=6)
speed_spin.pack(side=tk.LEFT)
speed_spin.delete(0, tk.END)
speed_spin.insert(0, "50")


tk.Button(frame_controls, text="Start", command=start_animation).pack(side=tk.LEFT, padx=5)
tk.Button(frame_controls, text="Stop", command=stop_animation).pack(side=tk.LEFT, padx=5)


label_coords = tk.Label(root, text="X: 0, Y: 100", font=("Arial", 12))
label_coords.pack(pady=5)

root.mainloop()
