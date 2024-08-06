def divide(x, y):
    # Handle division by zero
    if y == 0:
        return "Error: Division by zero is undefined."
    return x / y

def subtract(x, y):
    return x - y

# Get input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Ask the user which operation to perform
operation = input("Enter 'divide' for division or 'subtract' for subtraction: ").strip().lower()

# Perform the chosen operation and print the result
if operation == 'divide':
    result = divide(x, y)
    print(f"The result of dividing {x} by {y} is: {result}")
elif operation == 'subtract':
    result = subtract(x, y)
    print(f"The result of subtracting {y} from {x} is: {result}")
else:
    print("Invalid operation")