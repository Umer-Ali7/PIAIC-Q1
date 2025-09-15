print("----------------Calculator----------------")

# Select operation
print("""Select operation:
      1. Addition (+)
      2. Subtraction (-)
      3. Multiplication (*)
      4. Division (/)
      """)

# Take input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Function
def calculator(num1, num2, operator):

    if operator == '+':
        num1 + num2
        return f"{num1} + {num2} = {num1 + num2}"
    elif operator == '-':
        num1 - num2
        return f"{num1} - {num2} = {num1 - num2}"
    elif operator == '*':
        num1 * num2
        return f"{num1} * {num2} = {num1 * num2}"
    elif operator == '/':
        num1 / num2
        return f"{num1} / {num2} = {num1 / num2}"
    else:
        return 'Invalid Operator'
    
calculator(num1=num1, num2=num2, operator=operation)

# Displaying the result
print(f"Result: {calculator(num1=num1, num2=num2, operator=operation)}")