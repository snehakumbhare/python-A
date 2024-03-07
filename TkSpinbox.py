#Python Tkinter Spinbox: Custom range and step size made easy

import tkinter as tk
from tkinter import ttk

def update_value():
    selected_value = spinbox_var.get()
    result_label.config(text=f"Selected Value: {selected_value}")

parent = tk.Tk()
parent.title("Spinbox Example")

# Create a Spinbox widget with a custom range and step size
spinbox_var = tk.DoubleVar()
spinbox = ttk.Spinbox(parent, from_=0.0, to=10.0, increment=0.5, textvariable=spinbox_var)
spinbox.pack(padx=20, pady=20)

# Create a button to get the selected value
get_value_button = tk.Button(parent, text="Get Selected Value", command=update_value)
get_value_button.pack()
# Create a label to display the selected value
result_label = tk.Label(parent, text="", font=("Helvetica", 10))
result_label.pack()
parent.mainloop()
