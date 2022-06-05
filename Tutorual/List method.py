numbers = [5, 2, 1, 5, 3]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(numbers)
print(numbers)
