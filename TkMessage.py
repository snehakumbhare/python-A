#Python Tkinter message widget: Multi-line text with word wrapping made easy

import tkinter as tk
parent = tk.Tk()
parent.title("Message Widget Example")
# Create a Message widget with word wrapping
message = tk.Message(parent, text="This is a multi-line text message widget.It automatically wraps text to fit within the specified width. Write a Python GUI program to create a Message widget for displaying multi-line text with word wrapping using tkinter module.", width=200)
message.pack(padx=20, pady=20)
parent.mainloop()
