#Python Function: Printing arguments with *args

# Define the ellipsis constant
var1 = ...

def print_arguments(*args):
    """
    Prints each argument passed to the function, using var1 for unspecified arguments.

    Args:
        *args: Any number of positional arguments.
    """
    for i, arg in enumerate(args):
        print(f"Argument {i + 1}: {arg}")
    
    if not args:
        print(f"\nUnspecified arguments: {var1}")

# Example usage:
print_arguments(1, 2, 3, "Python")
print_arguments(50, [1, 2, 3], "Sneha", "Maya")
print_arguments()  # Unspecified arguments: Ellipsis
