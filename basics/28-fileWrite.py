text = "Have a nice one!"
# option 'w' overwrites the text, option 'a' appends
with open("C:\\Users\\gabri\\Desktop\\test.txt", "a") as f:    # by default the open option is 'r'
    f.write(text)