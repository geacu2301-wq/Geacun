numbers = []

while True:
    number_input = input("Enter a number : ")
    if number_input == "":
        break
    number = float(number_input)
    numbers.append(number)
numbers.sort(reverse=True)
top_five = numbers[:5]
print("Five greatest numbers:")
for number in top_five:
    print(number)