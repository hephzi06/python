# i = 0;
# while i < 10:
#     command = input('> ').lower()
#     if command == "help":
#         print("> Start")
#         print("> Stop")
#         print("> quit")
#     elif command == "start":
#         print("Car is starting ......")
#     elif command == "stop":
#         print("Car is stopping ......")
#     elif command == "quit":
#         break


# or
# Mosh correction
"""correction by mosh"""

command = ""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":

        if started:
            print("Car is already started")
        else:
            started = True
            stopped = False
            print("Car started ...")
    elif command == "stop":
        if stopped:
            print("Car already stopped")
        else:
            started = False
            stopped = True
            print("Car stopped .. ")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that")
