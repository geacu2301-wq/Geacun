def sum_list(numbers):
    total=0
    for number in numbers:
        total=total+number
        return total
    my_list=[23,1,2007]
    result=sum_list(my_list)
    print("The sum of the list is :", result)