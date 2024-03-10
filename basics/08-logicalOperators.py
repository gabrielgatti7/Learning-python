# and, or, not

temp = int(input("What's the temperature outside in Celsius?: "))

# if temp >= 20 and temp <= 30:
#     print("The temperature is good!\nGo outside!")
# elif temp < 20 or temp > 30:
#     print("The temperature is bad today!\nStay inside!")

if not(temp >= 20 and temp <= 30):
    print("The temperature is bad today!\nStay inside!")
elif not(temp < 20 or temp > 30):
    print("The temperature is good!\nGo outside!")
