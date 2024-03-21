#Python Tkinter: Creating a custom input dialog

import tkinter as tk
from tkinter import simpledialog

def show_name_dialog():
    name = simpledialog.askstring("Input", "Input your name:")
    if name:
        name_label.config(text=f"Hello, {name}!")

parent = tk.Tk()
parent.title("Input Dialog Example")

get_name_button = tk.Button(parent, text="Get Name", command=show_name_dialog)
get_name_button.pack(padx=20, pady=20)

name_label = tk.Label(parent, text="", padx=20, pady=10)
name_label.pack()

parent.mainloop()
