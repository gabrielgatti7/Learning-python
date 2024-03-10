# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item)) # positional argument
print("The {animal} jumped over the {item}".format(animal="dog", item="bike")) # keyword argument

text = "The {} jumped over the {}"
print(text.format(animal, item))
print()


# PADDING
name = "Gabriel"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you!".format(name))
print("Hello, my name is {:<10}. Nice to meet you!".format(name))
print("Hello, my name is {:>10}. Nice to meet you!".format(name))
print("Hello, my name is {:^10}. Nice to meet you!".format(name))

# NUMBERS
pi = 3.141592653589793
print("Pi = {:.3f}".format(pi))

x = 1000
print("x = {:,}".format(x))
print("x = {:b}".format(x)) # binary
print("x = {:o}".format(x)) # octal
print("x = {:X}".format(x)) # hexadecimal
print("x = {:e}".format(x)) # scientific notation
