# slicing = create a substring by extracting elements from another string
# operators -> indexing[] or slice()
# [start:stop:step]

name = "Gabriel Gatti"

first_name = name[:7] # or [0:7]
last_name = name[8:] # or [8:13]
funky_name = name[::3] # or [0:13:3]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

# slice creates an object

website1 = "https://www.youtube.com"
website2 = "https://www.wikipedia.com"

slice = slice(12,-4)

print(website1[slice])
print(website2[slice])