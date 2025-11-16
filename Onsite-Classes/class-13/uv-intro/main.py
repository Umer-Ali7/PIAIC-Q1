from rich import print

# print("Hello [bold green]World![/bold green]")

# #Four pillars of OOP: Encapsulation, Abstraction, Inheritance, Polymorphism

# --- OOP ---
# class Car:
#     def __init__(self, name, model, year, color):   # constructor
#         self.name = name
#         self.model = model
#         self.year = year
#         self.color = color
        # self.__price = 300000  # private attribute

    # def display_info(self):
    #     print(
    #         f"Car Name: {self.name}, Model: {self.model}, Year: {self.year}, Color: {self.color}"
    #     )

    # def get_price(self):    # getter method
    #     return self.__price
    
    # def set_price(self,):   # setter method
    #     new_price = 200000
    #     self.__price = new_price


# car1 = Car("G-Wagon", "G63", 2024, "Black")
# print(f"[bold Yellow]{car1.name, car1.model} [/bold Yellow] {Car.display_info(car1)}")

# car2 = Car("Range Rover", "Sport", 2023, "White")
# print(f"[bold Blue]{car2.name, car2.model} [/bold Blue] ")

# car3 = Car("BMW", "X5", 2022, "Silver")
# print(f"[bold Red]{car3.name, car3.model} [/bold Red] ")

# car4 = Car("Audi", "Q7", 2021, "Grey")
# print(f"[bold Magenta]{car4.name, car4.model} [/bold Magenta] ")


# print(f"Car1 Price: {car1.get_price()}")
# car1.set_price()
# print(f"Car1 New Price: {car1.get_price()}")

# --- Inheritance ---
class Car:
    def __init__(self, name, model, year, color):   # constructor
        self.name = name
        self.model = model
        self.year = year
        self.color = color

class ElectricCar(Car):  # child class
    def __init__(self, name, model, year, color, battery_capacity):
        super().__init__(name, model, year, color)
        self.battery_capacity = battery_capacity

electric_car1 = ElectricCar("Tesla", "Model S", 2024, "Red", "100 kWh")
print(f"[bold Cyan]{electric_car1.name, electric_car1.model} [/bold Cyan] ")