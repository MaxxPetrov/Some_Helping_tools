

class Vehicle:
    def __init__(self, max_speed, mileage, color, make):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        self.make = make

    def method1(s):
        print(f"this is good {s.color}")

    def method2(max2):
        print(f"The make of my car is {max2.make}")


car1 = Vehicle()
col = input("Enter color")
car1.color = col

car1 = Vehicle(120, 50, "white", "tesla")
car2 = Vehicle(150, 80, "Black", "Volga")

car1.max_speed = 777777
# car2.color = "night"

car1.method1()


