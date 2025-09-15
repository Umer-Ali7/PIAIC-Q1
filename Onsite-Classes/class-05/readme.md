# 📘 Class 05 – Python Functions & Prompt Engineering  

**Date:** Sunday, September 14, 2025  
**Instructors:** Sir Aneeq & Sir Hamza  

---

## 🎯 Topics Covered  

### 🐍 Python  
1. **Functions Basics**  
   - How to define a function using `def`.  
   - Calling functions multiple times.  

2. **Parameters & Arguments**  
   - Positional arguments.  
   - Keyword arguments.  
   - Default parameter values.  

3. **Examples from Class**  
   ```python
   # Function without parameters
   def greet():
       print('Hello, World')
       print('Open Door!')

   greet()
   greet()

   # Function with parameters
   def sum(num1, num2):
       print(num1 + num2)

   sum(num1=100, num2=200)  # keyword arguments

   # Function with return value
   def catch(obj='⚽'):
       return f'Catched! {obj}'

   bag = catch('💻')
   print(bag)  # Output: Catched! 💻


## List Methods Recap

- len() → Count elements in list.

- remove() → Remove by value.

- pop() → Remove by index.

- insert() → Insert at specific position.

- List slicing (list[start:end]).

## 🤖 Prompt Engineering
### 1. Introduction – What is Prompt Engineering?
### 2. Understanding LLMs (Large Language Models).
### 3.Essential Configurations
- Temperature
- Token Limits
- Output Length
### 4. Prompting Techniques
- Zero-shot
- One-shot
- Few-shot
- System / Role prompting
- Chain of Thought (CoT)
### 5. Example: Prompt Coach
### 6. Image Generation Example: Neno Banana 🍌

## 📝 Homework
- Create a simple calculator using a <b>function with return value</b>.
- Function should accept 3 parameters: `num1`, `num2`, `operator`.
- Use if/else to handle operations (`+, -, *, /`).

✨ From writing Python functions to engineering prompts — building the AI mindset step by step 🚀