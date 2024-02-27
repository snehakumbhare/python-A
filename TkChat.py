#Create a chat application interface with Python Tkinter

import tkinter as tk

# Function to send a message
def send_message():
    message = message_entry.get()
    if message:
        message_history.config(state=tk.NORMAL)
        message_history.insert(tk.END, f"You: {message}\n")
        message_history.config(state=tk.DISABLED)
        message_entry.delete(0, tk.END)

# Create the main window
parent = tk.Tk()
parent.title("Chat Application")

# Create a Text widget for message history
message_history = tk.Text(parent, wrap=tk.WORD, width=40, height=10)
message_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
message_history.config(state=tk.DISABLED)

# Create an Entry widget for entering messages
message_entry = tk.Entry(parent, width=30)
message_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a "Send" button
send_button = tk.Button(parent, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the Tkinter event loop
parent.mainloop()
