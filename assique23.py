#Create a function that inputs user's phone number.
#  Raise an exception if phone number has less than 10 digit 
def func():
    try:
        value = int(input("Please enter a number: "))
        if len(str(value)) < 10:
            raise ValueError  # Raise exception if value is less than 10 digit
    except ValueError: # catch and handle exception
        print("Oops!  That was no valid number.  Try again...")
func()