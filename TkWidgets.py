#Python tkinter widgets Exercise: Create a Combobox with three options using tkinter module

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_str_var = tk.StringVar()

my_combobox = ttk.Combobox(
    root, textvariable = my_str_var,
    values=["PHP", "Java", "Python" ,"SQL", "Django", "Angular10", "Web Designing",])

my_combobox.pack()
root.mainloop()


