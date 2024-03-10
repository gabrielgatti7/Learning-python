# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "gabriel Gatti!"

if name[0].islower():
    name = name[0].capitalize() + name[1:]

first_name = name[:7].upper()
last_char = name[-1:]

print(name)
print(first_name)
print(last_char)