import tkinter as tk
from tkinter import ttk

class ThemedLabel(ttk.Label):
    def __init__(self, master=None, text="", font=("Arial", 12), fg="white", bg="blue", **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.config(
            font=font,      # Set the font
            foreground=fg,  # Set the text color
            background=bg  # Set the background color
        )

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Themed Label Example")

    # Create a themed label with custom font, text color, and background color
    themed_label = ThemedLabel(root, text="Python Exercises", font=("Helvetica", 16), fg="red", bg="yellow")
    themed_label.pack(padx=20, pady=20)
    themed_label = ThemedLabel(root, text="Java Exercises", font=("Verdana", 14), fg="green", bg="blue")
    themed_label.pack(padx=20, pady=20)
    themed_label = ThemedLabel(root, text="C++ Exercises", font=("Courier ", 12), fg="white", bg="orange")
    themed_label.pack(padx=20, pady=20)
    root.mainloop()
