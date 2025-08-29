#  i am printing hello world
#  now i will write some more code
#  then will tell what it is doing

print("Hello world")

#  variables
name = "Aneeq"
number = 10
print(number)

# data types
# 1- string
# 2- integer
# 3- boolean
# 4- float
# 5- list
# 6- dictionary
# 7- set
# 8- tuple

# 1- String -> str
print("Aneeq")

# 2- Integer -> int
print(5)

# 3- float -> float
print(5.5)

# 4- Boolean ->  bool -> True / False
print(False)

user_name = "Aneeq"
name_type = type(user_name)
print(name_type)

number = 20
print(type(number))

floating_number = 2.4
print(type(floating_number))

boolean_number = True
print(type(boolean_number))

# Operators

#       2 = operand  , + = operator
# print(2 + 2)


# 1- Arithmetic Operators
# 2- Comparison Operators
# 3- Assignment Operators
# 4- Logical Operators

# Arithmetic Operators

# Additions ->  +
# subtraction -> -
# Mutliplication -> *
# Divison -> /
# Modulus -> %
# Floor Division ->//
# Exponention -> **


print(2 + 2) # Addition
print(10 - 5) # Subtraction
print(10 * 2) # Mutliplication
print(20 / 2 ) # Division
print(10 // 3) # Floor Divsion
print(10 % 3)  # Modulus -> 10 - 3 = 7 - 3 = 4- 3 =1
print(2 ** 3) # Exponention -> 2 * 2 * 2 = 8

# 2- Comparison Operators

# equal to -> ==
# greater than -> >
# less than -> <
# not equal -> !=
# greater equal to -> >= -> ya to zyada he ya phr baraber he
# less than equal to -> <=  -> ya to kam he ya phr baraber he

num1 = 10
num2 = 5


print(num1 == num2) # meri dono value baraber hen ->  False
print(num1 > num2) # num1 ki value num2 se zyada he -> True
print(num1 < num2) # num1 ki value num2 se kam he ->  False
print(num1 != num2) # num1 jo he num2 k baraber nahi he -> True

# Assignment Operators
# equal to -> =
# =	x = 5	x = 5


name = "Aneeq"

num1 = 20
# num2  = 20 + 5
num2 = num1 + 5  # 20 + 5 =  25
print(num2)
num3 = num1 - 5 # 20-5 = 15
print(num3)
num4 = num1 * 5 # 20 * 5 = 100
print(num4)
num5 = num1 / 5 # 20 / 5 =  4.0
print(num5)

# Logical Operators
#  Logical And -> and
# Logical Or -> or
# Logical Not -> not

num1 = 10
num2 = 20

# condition = num1 baraber na ho num2 k   and   num1  chota ho num2 se
result = num1 != num2 and num1 < num2
print(result)
#           True        and  False
result2 = num1 != num2 and num1 > num2
print(result2)
#          True         ya   False
result3 = num1 != num2 or num1 > num2
print(result3)

num1 = 10
num2 = 20
print(num1,num2)
# print("num1 is", num1)
print("num1 added by num2", num1+num2 )