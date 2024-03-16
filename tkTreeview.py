#Python Tkinter Treeview widget: Sorting and columns made easy
import tkinter as tk
from tkinter import ttk

# Function to sort the Treeview by column
def sort_treeview(tree, col, descending):
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    data.sort(reverse=descending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)
    tree.heading(col, command=lambda: sort_treeview(tree, col, not descending))

parent = tk.Tk()
parent.title("Sortable Treeview Example")

# Create a Treeview widget with columns
columns = ("Name", "Age", "Country")
tree = ttk.Treeview(parent, columns=columns, show="headings")

# Configure column headings and sorting functionality
for col in columns:
    tree.heading(col, text=col, command=lambda c=col: sort_treeview(tree, c, False))
    tree.column(col, width=100)

# Insert data into the Treeview
data = [("Sachin", 35, "Jaipur"),
        ("Sneha", 28, "Bhopal"),
        ("Maya", 45, "Nagpur"),
        ("Siya", 38, "Pune"),
        ("Ram", 32, "Dwaraka"),
        ("Radha", 30, "Ujjain"),
        ("Krishna", 42, "Indore"),
        ("Neha", 30, "Rewa")]

for item in data:
    tree.insert('', 'end', values=item)
tree.pack()
parent.mainloop()
