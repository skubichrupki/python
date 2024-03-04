import tkinter as tk

root = tk.Tk()
root.title("hi")

width = 480
height = 360
root.geometry(f"{width}x{height}")

label = tk.Label(root, text="hi")
label.pack()

def on_button_click():
    label.config(text="button clicked!")

button1 = tk.Button(root, text="click here", command=on_button_click)
button1.pack()

def move_element():
    button1.place(x=width/2, y=height/2)

move_element()
root.mainloop()


