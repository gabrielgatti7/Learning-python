food = ["pizza", "hamburger", "lasagna", "bread"]

print(food)
print(type(food))
# print(food[0])

food.append("chicken")
food.remove("hamburger")
food.pop()
food.insert(0, "chicken")
food.sort()
# food.clear()

for i in food:
    print(i)