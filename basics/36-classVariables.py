# instance variable = declared inside of a constructor and they can be given unique values
# class variable    = declared within the class but outside of the constructor, so a default value
#                     can be set for all instances of this class
class Car:
    wheels = 4              # class variable

    def __init__(self, make, model, year, color):
        self.make = make    # instance variable
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable


car_1 = Car("Chevrolet", "Corvette", 2021, "red")
car_2 = Car("Ford", "Mustang", 2022, "black")

car_1.wheels = 2
# Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
print(Car.wheels)