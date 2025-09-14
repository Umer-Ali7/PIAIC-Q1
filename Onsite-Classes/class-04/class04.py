firstName: str = input("What is your first name: ")
lastName: str = input("What is your last name: ")
age: int = input("What is your age: ")

print(firstName, lastName, ",and your age is:",age)

#best practice
first_name: str = input("What is your first name: ")
last_name: str = input("What is your last name: ")
age: int = input("What is your age: ")
# print(first_name, last_name, ",and your age is:",age)
print(f"{first_name} {last_name} ,and your age is: {age}")  # f string  / Concatenation 
# Umer Ali , and your age is: 17

fav = "mango"
print( fav )
fav = "banana"
print( fav )