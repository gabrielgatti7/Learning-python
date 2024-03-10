# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

username = ["gabriel", "john", "smith"]
password = ("p@ssword", "1234", "abcd")
login_date = ["1/1/2023", "15/5/2023", "14/1/2024"]

# users = zip(username, password)
# users = list(zip(username, password))
users = zip(username, password, login_date)
# print(type(users))
#
for i in users:
    print(i)


# users = dict(zip(username, password))
#
# for key,value in users.items():
#     print(key+" : "+value)
