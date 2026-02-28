def remove_odd(numbers):
    new_list=[]
    for number in numbers:
        if number % 2== 0:
            new_list.append(number)
    return new_list

variable_list = [1, 2, 3, 4, 5, 6, 7]
cut_list = remove_odd(variable_list)
print("Original list:", variable_list)
print("New list:", cut_list)