# Define functions for basic arithmetic operations
def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference between x and y."""
    return x - y

def multiply(x, y):
    """Return the product of multiplying x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y, or an error message if dividing by zero."""
    try: 
        return x / y
    except ZeroDivisionError:
        return "You cannot divide by zero. Sorry!"


def calculator():
    """Run a simple command-line calculator that performs basic arithmetic operations."""
    while True:
        # Display a menu with available operations
        print("Select operation:")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")

        # Get the user's choice of operation
        user_choice = input("Enter the number of your choice: ")

        # Exit the calculator if the user chooses to quit
        if user_choice == "5":
            print("Bye! See you soon!")
            break
        
        # Get the numbers to perform the operation on
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        # Perform the selected operation and display the result
        if user_choice == "1":
            print("Result:", add(num1, num2))

        elif user_choice == "2":
            print("Result:", subtract(num1, num2))

        elif user_choice == "3":
            print("Result:", multiply(num1, num2))

        elif user_choice == "4":
            print("Result:", divide(num1, num2))
        else: 
            print("Invalid input. Please try again")
        
# Run the calculator if the script is being executed as the main program
if __name__ == "__main__":
    calculator()