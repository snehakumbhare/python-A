#Create a Python login form with Tkinter's grid manager
import tkinter as tk

# Create a function to handle the login button click event
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user1" and password == "abcd123":
        login_status.config(text="Login successful", fg="green")
    else:
        login_status.config(text="Login failed. Try again.", fg="red")

# Create the main Tkinter window
parent = tk.Tk()
parent.title("Login Form")

# Create labels and Entry widgets for username and password
username_label = tk.Label(parent, text="Username:")
password_label = tk.Label(parent, text="Password:")
username_entry = tk.Entry(parent)
password_entry = tk.Entry(parent, show="*")  # Show '*' for password entry

# Create a Login button
login_button = tk.Button(parent, text="Login", command=login)

# Create a label to display login status
login_status = tk.Label(parent, text="", fg="black")

# Use the Grid geometry manager to arrange widgets
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="E")
username_entry.grid(row=0, column=1, padx=10, pady=5)
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="E")
password_entry.grid(row=1, column=1, padx=10, pady=5)
login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
login_status.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
# Run the Tkinter main loop
parent.mainloop()
