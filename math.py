def multiply(x, y):
    return x * y

def add(x, y):
    return x + y

# Get input from the user
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Ask the user which operation to perform
operation = input("Enter 'multiply' for multiplication or 'add' for addition: ").strip().lower()

# Perform the chosen operation and print the result
if operation == 'multiply':
    result = multiply(x, y)
    print(f"The result of multiplying {x} and {y} is: {result}")
elif operation == 'add':
    result = add(x, y)
    print(f"The result of adding {x} and {y} is: {result}")
else:
    print("Invalid operation")