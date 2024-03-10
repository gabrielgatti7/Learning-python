# tuple = collection which is ordered and unchangeable used to group
#         together related data

student = ("Gabriel", 22, "Male")

print(type(student))
print(student.count("Gabriel"))
print(student.index(22))

for i in student:
    print(i)

if "Male" in student:
    print("Student's gender is: Male")