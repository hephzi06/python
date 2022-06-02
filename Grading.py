grade = int(input("Enter your grade score: "))
if 75 <= grade <= 100:
    print(f"Excellent your score is {grade}")
elif 60 <= grade:
    print(f'Very Good your score is {grade}')
elif 45 <= grade:
    print(f'Bad score but you can rewrite the exam. Do you want to know your score? ')
    pick = input("(Y)es or (N)o: ").lower()
    if pick == "y":
        print(f'Your score is {grade}')
    elif pick == "n":
        print(f"Don't forget to retake the exam. ")
else:
    print(f'You failed. Do you want to know your score?')
    pick = input("(Y)es or (N)o: ").lower()
    if pick == "y":
        print(f'Your score is {grade}')
    elif pick == "n":
        print(f"Don't forget to retake the exam")