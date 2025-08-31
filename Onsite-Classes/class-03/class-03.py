fav_game = "pubg"
fav_food = "Biryani"
age = True

id(fav_game)

print(fav_game, id(fav_game))

# if-else

isRaining = True

if isRaining:
    print("School nhi Jana he")
else:
    print("School Jana he")

age = 15

print(age == 18) - True
print(age < 18) - False

if age == 18:
    print("You can vote")
else:
    print("koi bat nhi chote next time")

if age >= 18:
  print("You can vote")
else:
    print("koi bat nhi chote next time")

# elif

number = 10

if number > 10:
    print("Number 10 se bara he")
elif number == 10:
    print("number 10 k barabar he")
else:
    print("number 10 se chota he")

# Class Task

percentag = int(input("Enter your percentag: "))

if percentag >= 80 and percentag < 100:
    print("A1 Grade")
elif percentag >= 70 and percentag < 80:
    print("A Grade")
elif percentag >= 60 and percentag < 70:
    print("B Grade")
elif percentag >= 50 and percentag < 60:
    print("C Grade")
else:
    print("Fail")
