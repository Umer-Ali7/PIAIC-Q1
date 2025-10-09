# Lambda Functions / Anonoymous Function


# def function_name(paramaters):
    # return statement / expression/ koi bhi kam ya value provide karna

def add(num1, num2):
    return num1 + num2

result = add(2, 5)

print(result)

# lambda paramaters:  statement / expression/

lambda num1, num2: num1 + num2

# store in variable 

# function name = lambda paramaters:  statement / expression/
add = lambda num1, num2: num1 + num2

print(add(10, 20))

# Dictionary type

user_dict = {
    "name": "Umer Ali",
    "roll_num": 1212,
    "age": 17
}

# print("User Data", user_dict)
print("User Name", user_dict["name"])
print("User Age is", user_dict["age"])


# Task

user_Data = {
    "name": "Umer Ali",
    "email": "Umerali9@gmail.com",
    "phone_num": "03052597198",
    "age": 17,
    "roll_num": 1212,
    "add": lambda num1, num2: num1 + num2
}

print("Add", user_Data["add"](5,6))