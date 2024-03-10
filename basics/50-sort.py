# sort() method   = used with lists
# sort() function = used with iterables

# EX 1
# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
#
# # students.sort(reverse=True)       # can be used when students is a list
# sorted_students = sorted(students, reverse=True)  # function sorted returns a list
#
# for i in sorted_students:
#     print(i)

# EX 2
# # list of tuples
# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78)]

# tuple of tuples
students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78))

grade = lambda grades: grades[1]
age = lambda ages: ages[2]
# students.sort(key=age)
sorted_students = sorted(students, key=grade)

for i in sorted_students:
    print(i)
