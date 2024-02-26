#Create an employee list application with Python Tkinter

import tkinter as tk

# Function to add a new contact to the Listbox
def add_contact():
    name = name_entry.get()
    if name:
        contacts_listbox.insert(tk.END, name)
        name_entry.delete(0, tk.END)

# Function to delete the selected contact from the Listbox
def delete_contact():
    selected_index = contacts_listbox.curselection()
    if selected_index:
        contacts_listbox.delete(selected_index)

# Create the main window
root = tk.Tk()
root.title("Employee List Application")

# Create a Listbox to display contacts
contacts_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
contacts_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an Entry widget to input new contacts
name_entry = tk.Entry(root)
name_entry.pack(pady=5)

# Create "Add" and "Delete" buttons
add_button = tk.Button(root, text="Add", command=add_contact)
add_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.pack(side=tk.LEFT, padx=5)

# Start the Tkinter event loop
root.mainloop()
