# filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

friends = [("Marcos", 16),
           ("João", 18),
           ("Maria", 17),
           ("Julia", 19),
           ("Gabriel", 22)]

# age = lambda data: True if data[1] >= 18 else False
age = lambda data: data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)