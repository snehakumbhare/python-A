#Python Tkinter calculator with file saving

import tkinter as tk
from tkinter import filedialog

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text=f"Result: {result}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

def save_result():
    result = result_label.cget("text")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file.write(result)
        except Exception as e:
            result_label.config(text=f"Error saving file: {str(e)}")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root)
entry.pack(padx=20, pady=10, fill="both", expand=True)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(padx=20, pady=10)

result_label = tk.Label(root, text="", padx=20, pady=10)
result_label.pack()

save_button = tk.Button(root, text="Save Result", command=save_result)
save_button.pack(padx=20, pady=10)
root.mainloop()
