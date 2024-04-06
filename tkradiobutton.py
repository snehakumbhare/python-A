#Customizing Tkinter radio buttons with distinct styles
import tkinter as tk
from tkinter import messagebox

class TraditionalRadioButtons:
    def __init__(self, root):
        self.root = root
        self.root.title("Traditional Radio Buttons")

        # Initialize the selected radio button index
        self.selected_option = tk.IntVar()
        self.selected_option.set(0)  # Initialize as no option selected

        # Create traditional radio buttons
        self.radio_button1 = tk.Radiobutton(root, text="Option 1", variable=self.selected_option, value=1, command=self.display_message)
        self.radio_button2 = tk.Radiobutton(root, text="Option 2", variable=self.selected_option, value=2, command=self.display_message)
        self.radio_button3 = tk.Radiobutton(root, text="Option 3", variable=self.selected_option, value=3, command=self.display_message)

        # Pack the radio buttons
        self.radio_button1.pack(pady=10)
        self.radio_button2.pack(pady=10)
        self.radio_button3.pack(pady=10)

    def display_message(self):
        selected_value = self.selected_option.get()
        if selected_value == 1:
            message = "Option 1 selected!"
        elif selected_value == 2:
            message = "Option 2 selected!"
        elif selected_value == 3:
            message = "Option 3 selected!"
        else:
            message = "No option selected!"
        
        messagebox.showinfo("Radio Button Selection", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = TraditionalRadioButtons(root)
    root.mainloop()
