i = 0;
while i < 10:
    command = input('> ').lower()
    if command == "help":
        print("> Start")
        print("> Stop")
        print("> quit")
    elif command == "start":
        print("Car is starting ......")
    elif command == "stop":
        print("Car is stopping ......")
    elif command == "quit":
        break
