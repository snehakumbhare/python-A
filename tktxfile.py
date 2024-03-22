#Python Tkinter text file writer: Create and save text files
import tkinter as tk
from tkinter import filedialog

def save_as_text_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        try:
            with open(file_path, 'w') as file:
                file_content = text_widget.get('1.0', tk.END)
                file.write(file_content)
                status_label.config(text=f"File saved as: {file_path}")
        except Exception as e:
            status_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("Text file writer")

text_widget = tk.Text(root, wrap=tk.WORD, height=15, width=35)
text_widget.pack(padx=20, pady=20)

save_button = tk.Button(root, text="Save As", command=save_as_text_file)
save_button.pack(padx=20, pady=10)

status_label = tk.Label(root, text="", padx=20, pady=10)
status_label.pack()

root.mainloop()
