#Python Tkinter Messagebox: Display messages
import tkinter as tk
from tkinter import messagebox

# Create the main window
parent = tk.Tk()
parent.title("Messagebox Example")

# Function to display a message in a messagebox
def show_message():
    messagebox.showinfo("Message", "Hello!")

# Create a button to trigger the messagebox
button = tk.Button(parent, text="Show Message", command=show_message)
button.pack()

# Start the Tkinter event loop
parent.mainloop()
