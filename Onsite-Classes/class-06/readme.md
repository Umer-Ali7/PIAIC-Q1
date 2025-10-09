# 🐍 Class 06 – Lambda Functions & Dictionaries  

**Course:** PIAIC – Modern AI with Python (Quarter 1)  
**Instructor(s):** Sir Aneeq & Sir Hamza  
**Date:** September 2025  

---

## 🎯 Topics Covered  

1. **Lambda Functions (Anonymous Functions)**  
   - Quick one-line functions without `def`.  
   - Syntax:  
     ```python
     lambda parameters: expression
     ```

2. **Using Lambda with Variables**  
   ```python
   add = lambda num1, num2: num1 + num2
   print(add(10, 20))   # Output: 30

3. **Dictionaries in Python**
    - Store data as key–value pairs.

    - Access values using keys.
    ```python
    user_dict = {
    "name": "Umer Ali",
    "roll_num": 1212,
    "age": 17
    }

    print("User Name:", user_dict["name"])  
    print("User Age:", user_dict["age"])  
    ```

4. **Combining Lambda with Dictionary**

- Functions can also be stored inside dictionaries.

- Example with a simple calculator function:

```python
user_Data = {
    "name": "Umer Ali",
    "email": "Umerali9@gmail.com",
    "phone_num": "03052597198",
    "age": 17,
    "roll_num": 1212,
    "add": lambda num1, num2: num1 + num2
}

print("Add:", user_Data["add"](5, 6))  # Output: 11
```

## ✅ Learning Outcomes

- Understood the difference between normal functions and lambda functions.

- Learned how to store and use functions inside dictionaries.

- Practiced real-world data structures (dictionary) for managing student info.

## 🚀 Class Task

- Create a dictionary with your own details (name, email, roll number, etc.).

- Add a lambda function inside the dictionary for any basic math operation.

- Print results to test your function.

*✨ This class helped us explore how Python can mix data + functions together in powerful ways! 🚀*