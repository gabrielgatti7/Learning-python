# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression (if/else) for item in iterable]

# EXAMPLE 1
squares = []                    # create an empty list
for i in range (1,11):          # create a for loop
    squares.append(i * i)       # define what each loop iteration should do
print(squares)

squares = [i * i for i in range (1,11)]
print(squares)


# EXAMPLE 2
# list = [expression for item in iterable if conditional]
students = [100,90,80,70,60,50,40]
# passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
print(passed_students)

# EXAMPLE 3
# list = [expression (if/else) for item in iterable]
passed_students = [i if i >= 60 else "FAILED" for i in students]
print(passed_students)
