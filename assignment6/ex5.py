def remove_odd(numbers):
    new_numbers = []
    for num in numbers:
        if num % 2 == 0:
            new_numbers.append(num)
    return new_numbers
numbers = [23,24,25,26,27,28,29,30]
result = remove_odd(numbers)
print("Original list:", numbers)
print("The new list after removing odd numbers:", result)
