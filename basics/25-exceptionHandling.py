# exception =    events detected during execution that interrupts the flow of a program

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    # print(type(result))
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers!")
except Exception as e:
    print(e)
else:                                   # if there are no exceptions
    print(result)
finally:
    print("This will always execute")
