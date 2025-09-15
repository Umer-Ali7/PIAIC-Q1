# List Methods and Functions in Python

vegitsbles = ["Hari Mirch", "lal mirch", "Alo", "Begun", "Moli"]

print(len(vegitsbles))
print(vegitsbles(-1))

vegitsbles.remove("Begun")
vegitsbles.pop(1)
vegitsbles.insert(2, "Dhanya")

print(vegitsbles[1:3])

print(vegitsbles)

# print(vegitsbles[1:3:4]) / ChatGPT


# Functions

def greet():
    print('Hello, World')
    print('Open Door!')

greet()
greet()


def sum(num1, num2):  # parameters

    print(num1 + num2)

sum(num1 = 100, num2 = 200) #   positional argument
sum()
sum()

def catch(obj='⚽'):
    # print(f'Catched! {obj}')

    return f'Catched! {obj}'

bag = catch('💻')

print(bag)


# Assignment Calculator
# def calculator(num1, num2, operator):

#     if operator == '+':
#         return num1 + num2
#     elif operator == '-':
#         return num1 - num2
#     elif operator == '*':
#         return num1 * num2
#     elif operator == '/':
#         return num1 / num2
#     else:
#         return 'Invalid Operator'