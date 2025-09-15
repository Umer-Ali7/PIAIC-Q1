# 🧮 Assignment – Class 05: Python Calculator  

**Course:** PIAIC – Modern AI with Python (Quarter 1)  
**Instructor(s):** Sir Aneeq & Sir Hamza  
**Date Assigned:** September 2025  

---

## 📌 Task  
Create a **simple calculator** using one function with `return`.  

- The function should take **three parameters**:  
  - `num1` → first number  
  - `num2` → second number  
  - `operator` → (+, -, *, /)  
- Use **if/else** conditions.  
- Function should handle all four operations: `+ - * /`.  

---

## ✅ Solution  

```python
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
        return f"{num1} + {num2} = {num1 + num2}"
    elif operator == '-':
        return f"{num1} - {num2} = {num1 - num2}"
    elif operator == '*':
        return f"{num1} * {num2} = {num1 * num2}"
    elif operator == '/':
        return f"{num1} / {num2} = {num1 / num2}"
    else:
        return 'Invalid Operator'

# Displaying the result
print(f"Result: {calculator(num1=num1, num2=num2, operator=operation)}")
```

## 🚀 Output Example
```
----------------Calculator----------------
Select operation:
      1. Addition (+)
      2. Subtraction (-)
      3. Multiplication (*)
      4. Division (/)

Enter first number: 10  
Enter second number: 5  
Enter operation (+, -, *, /): *  
Result: 10 * 5 = 50
```

## 🎯 Learning Outcomes
- Learned how to create functions with parameters.
- Practiced if/else logic for multiple conditions.
- Built a reusable calculator function in Python.

