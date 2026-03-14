numbers = []

def read_number():
    print("Enter the number (press enter to stop):")

    while True:
        num = input()

        if num == "":
            break

        numbers.append(float(num))
    numbers.sort(reverse=True)
    top_five = numbers[:5]
    print("The five greatest numbers are:")
    for num in top_five:
        print(num)
read_number()        
    
    