#Organize widgets with Python Tkinter's grid manager
import tkinter as tk

# Create the main Tkinter window
parent = tk.Tk()
parent.title("Widgets with Grid")

# Create label widgets
label1 = tk.Label(parent, text="Label 1", padx=10, pady=5, bg="lightblue")
label2 = tk.Label(parent, text="Label 2", padx=10, pady=5, bg="lightgreen")
label3 = tk.Label(parent, text="Label 3", padx=10, pady=5, bg="lightyellow")
# Create a button
button = tk.Button(parent, text="Click Me", padx=10, pady=5, bg="orange", command=parent.quit)
# Use the Grid geometry manager to arrange widgets
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)
button.grid(row=2, column=0, columnspan=2)
# Run the Tkinter main loop
parent.mainloop()
