# daemon thread = a thread that runs in the background, not important for program to run
#                 Your program will not wait for daemon threads to complete before exiting
#                 Non-daemon threads cannot normally be killed, stay alive until task is complete

#                 ex. background tasks, garbage collection, waiting for input, long running process

import threading
import time

def timer():
    print()
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logged in for: ", count, "seconds")

x = threading.Thread(target=timer, daemon=True)
# or x.setDaemon(True)
x.start()

print(x.isDaemon())

answer = input("Do you wish to exit?")