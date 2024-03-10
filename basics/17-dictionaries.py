# changeable unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {"Brazil":"Rio de Janeiro",
            "France":"Paris",
            "India":"New Dehli"}

capitals.update({"Japan":"Tokyo"})
capitals.update({"Brazil":"Brasilia"})
capitals.pop('France')

print(type(capitals))
print(capitals["Brazil"])
# print(capitals["Germany"])
print(capitals.get('Germany'))
print(capitals.items())
print(capitals.keys())
print(capitals.values())

for key, value in capitals.items():
    print(key, value)