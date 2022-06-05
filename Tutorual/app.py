secret_number = 9
guessLimit = 3
guessCount = 0
while guessCount < guessLimit:
    number = int(input("Guess: "))
    guessCount += 1
    if number == secret_number:
        print("You guessed it right")
        break

else:
    print("Sorry, you failed")
