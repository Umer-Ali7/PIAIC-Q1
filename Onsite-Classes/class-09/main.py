students = ["Ali", "Osama", "Sara"]
students.append("Arham")
students.append("Hamzah")

# Ali
for std in students:
    print(std)

# Task
for i in range(1, 101):
    print(i)

#task part 2
for i in range(1, 101, 2):
    print(i)

# task print table of 10
for i in range(1, 11):
    print(f"7 X {i} = {i * 7}")

#While loop

i = 1

while i <= 10:
    print(i)
    i = i + 1

# number guessing game
import random

random_num = random.randint(1, 100)


while True:
    user_input = int(input("Guess a number between 1 and 100: "))
    if user_input < random_num:
        print("Too low! Try again.")
    elif user_input > random_num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number. 🎉")
        break

#tuples

colors_list = ["green", "yellow", "red"]    # mutable
colors_tuple = ("green", "yellow", "red")   # immutable

colors_list[0] = "purple"
colors_tuple[0] = "purple"
print(colors_list)

week_lsit = ["monday",
             "tuesday",
             "wednesday",
             "thursday",
             "friday",
             "saturday",
             "sunday"]

week_tuple = ("monday",
             "tuesday",
             "wednesday",
             "thursday",
             "friday",
             "saturday",
             "sunday")

week_lsit[0] = "Birthday"

print(colors_list[0])
print(colors_tuple[0])

#task
for week in week_lsit:
    print(week)


# set
fruits_list = ["apple", "mango", "apple", "graps", "apple"]
fruits_set = {"apple", "mango", "apple", "graps", "apple"} # Dublicate remove

print(fruits_list[0])
print(fruits_set[0])

print(f"fruits ka list {fruits_list}")
print(f"fruits ka set {fruits_set}")

print("mango" in fruits_set)

fruits_set.add("banana") 
# print(fruits_set)

# task
user_input = input("Enter Fruite: ")
# print(user_input in  fruits_set)

if user_input in fruits_set:
    print(f"{user_input} he list me")
else:
    print("fruit dose not exit")

#try except
try:
    first_name = "Hamzah"
    print(10 / 0)
except Exception as err:
    print(err)