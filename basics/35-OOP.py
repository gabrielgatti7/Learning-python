# object = instance of a class
# an object has attributes = what an object is/has (ex: name, age, height)
# and methods = actions, what an object can do (ex: eat, sleep)
# class = describe what attributes and methods an object will have

from car35 import Car

car_1 = Car("Chevrolet", "Corvette", 2021, "red")
car_2 = Car("Ford", "Mustang", 2022, "black")

# print(car_1.make)
# print(car_1.model)
# print(car_1.year)
# print(car_1.color)

car_1.drive()
car_2.stop()
