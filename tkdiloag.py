#Python Tkinter: Creating an exit confirmation dialog
import tkinter as tk
from tkinter import messagebox
def confirm_exit():
    response = messagebox.askyesnocancel("Confirm Exit", "Want to save changes before exiting?")
    if response is None:
        # User clicked "Cancel"
        return
    elif response:
        # User clicked "Yes,"  
        save_changes()
    # Close the application
    root.destroy()

def save_changes():
    # Implement your save changes logic here
    messagebox.showinfo("Saved", "Saved successfully!")

root = tk.Tk()
root.title("Exit Example")
exit_button = tk.Button(root, text="Exit", command=confirm_exit)
exit_button.pack(padx=20, pady=20)
root.mainloop()

