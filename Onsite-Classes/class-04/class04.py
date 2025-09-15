# 🟢 Taking input from user
first_name: str = input("What is your first name: ")
last_name: str = input("What is your last name: ")
age: int = input("What is your age: ")

# Different ways of printing
print(first_name, last_name, ",and your age is:", age)  
print(f"{first_name} {last_name}, and your age is: {age}")  # f-string formatting

# 🟢 String concatenation and numbers
print("1" + "1")   # Concatenation of strings → 11
print("1+1")       # Prints as text → 1+1
print(1 + 1)       # Adds numbers → 2

# 🟢 Variables can be updated
fav = "Mango"
print(fav)
fav = "Banana"
print(fav)

# -------------------------------
# 📘 Lists in Python
# -------------------------------

# Old way (multiple variables)
fav_fruit1 = "Mango"
fav_fruit2 = "Orange"
fav_fruit3 = "Grapes"
fav_fruit4 = "Banana"

# Better way (using list)
# Index positions → 0         1         2         3
fruit_list = ["Mango", "Orange", "Grapes", "Banana"]
print("List before update:", fruit_list)

# Accessing list items
print(fruit_list[0])  # Mango
print(fruit_list[1])  # Orange
print(fruit_list[2])  # Grapes
print(fruit_list[3])  # Banana

# -------------------------------
# 🟢 Updating list values
fruit_list[1] = "Apple"        # Replaces Orange with Apple
print("List after update:", fruit_list)

# -------------------------------
# 🟢 Mixed list
mixed_list = ["Apple", 20, True, 2.4]
print("Before adding:", mixed_list)

mixed_list.append("Banana")     # Add Banana at the end
mixed_list.insert(2, "Apple")   # Add Apple at index 2
print("After adding:", mixed_list)

# -------------------------------
# 📘 List Methods
# -------------------------------
# 1. append() – Add at end
# 2. insert() – Insert at index
# 3. remove() – Remove by value
# 4. pop() – Remove by index (last if not specified)
# 5. sort() – Sort ascending
# 6. reverse() – Reverse order
# 7. index() – Find index of first occurrence
# 8. clear() – Remove all elements
# 9. extend() – Add elements from another iterable
# 10. copy() – Shallow copy of list
# 11. count() – Count occurrences of value
# len() – (not method) → total elements in list

# 🟢 Append Example
number_list = [1, 2, 3, 4, 5]
print("Before append:", number_list)
number_list.append(7)
print("After append:", number_list)

# 🟢 Insert Example
number_list = [1, 2, 4, 5]
print("Before insert:", number_list)
number_list.insert(2, 3)  # Insert 3 at index 2
print("After insert:", number_list)

# 🟢 Remove Example
number_list = [1, 2, 3, 4, 5]
print("Before remove:", number_list)
number_list.remove(2)  # Removes value 2
print("After remove:", number_list)

# 🟢 Length of list
numbers = [1, 2, 3, 4, 5]
print("List:", numbers)
print("Length of list:", len(numbers))

# 🟢 Pop Example
number_list = [1, 2, 3, 4, 5]
print("Before pop:", number_list)
number_list.pop(2)  # Removes element at index 2
print("After pop:", number_list)
