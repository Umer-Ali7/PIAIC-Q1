print("""
Assignment  01 
Topics: Variables, Data types, Operators
""")
print("--------------------------------")
print("Q1: Variables & Data Types")
name: str = "Umer Ali"  # string
age: int = 16   # integer
is_student: bool = True # boolean
print(name, age, is_student)    # printing variables
print(type(name), type(age), type(is_student))  # printing data types

print("--------------------------------")

print("Q2: Arithmetic Operators")
x: int = 20
y: int = 6
print(f"Addition: {x + y}")   # Addition
print("Subtraction:", x - y)    # Subtraction
print("Multiplication:", x * y) # Multiplication
print("Division:", x / y)   # Division
print("Floor Division:", x // y)  # Floor Division
print("Modulus:", x % y)    # Modulus
print("Exponentiation:", x ** y)    # Exponentiation


print("--------------------------------")

print("Q3: Assignment Operators")

num: int = 10
num += 5   # Add 5 to num
print("Add 5 to num:", num)  # Add 5 to num
num *= 2  # Multiply num by 2
print("Multiply num:", num)  # Multiply num by 2
num -= 4  # Subtract 4 from num
print("Subtract 4 from num:", num)  # Subtract 4 from num
print("Final value of num:", num)  # Final value of num

print("--------------------------------")

print("Q4: Comparison Operators")
a: int = 15
b: int = 12
print("The Value of a is 15 and b is 12")
print("a Greater than b:", a > b)  # Greater than
print("a Less than b:", a < b)  # Less than
print("a is equal to b:", a == b)  # Equal to
print("a is not equal to b:", a != b) # Not equal to
print("a Greater than or equal to b:", a >= b)  # Greater than or equal to
print("a Less than or equal to b:", a <= b)  # Less than or equal to

print("--------------------------------")

print("Q5: Logical Operators")
p: bool = True
q: bool = False
print("The Value of p is True and q is False")
print("and Operator:", p and q)  # and Operator
print("or Operator:", p or q)    # or Operator
print("not Operator:", not p)  # not Operator
print("not Operator:", not q)  # not Operator

print("--------------------------------")

print("Q6: Real-life example")

notebook_Price = 80  # Price of a notebook
quantity = 7 # Quantity of notebooks
total_Cost = notebook_Price * quantity # Total cost calculation
cash_in_hand = 600  # Cash in hand
print("Price of one notebook:", notebook_Price)
print("Quantity of notebooks:", quantity) 
print("Total cost of notebooks:", total_Cost) # print Total Cost
print("Is cash in hand enough to buy notebooks?:", cash_in_hand >= total_Cost)  #Final Result in a clear Message

print("--------------------------------")

print("Q7: Bonus (OPTIONAL)")

num1: int = input("Enter first number: ")
num2: int = input("Enter second number: ")

print(f"The sum of {num1} and {num2} is: {int(num1) + int(num2)}")  # Sum of two numbers
print(f"The {num1} is greater than {num2} or not?: {int(num1) > int(num2)}") # Comparison of two numbers

