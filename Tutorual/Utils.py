def find_max(numbers):
    maximum = numbers[0]
    for nums in numbers:
        if nums > maximum:
            maximum = nums
    return maximum