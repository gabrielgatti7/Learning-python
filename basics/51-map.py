# map() = applies a function to each item in an iterable (list, tuple, etc.)
#
# map(funtion, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jacket", 50.00),
         ("socks", 10.00)]

to_real = lambda data: (data[0], data[1]*4.92)

store_real = list(map(to_real, store))

for i in store_real:
    print(i)
