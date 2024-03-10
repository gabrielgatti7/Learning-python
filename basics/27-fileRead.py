# 'with' closes the file automatically
try:
    with open("C:\\Users\\gabri\\Desktop\\test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")

# print(file.closed)