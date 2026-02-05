# Converts inches to centimeters until a negative value is entered.

INCH_TO_CM = 2.54

while True:
    inches = float(input("Enter inches (negative to quit): "))
    if inches < 0:
        break
    centimeters = inches * INCH_TO_CM
    print(inches, "inches =", centimeters, "cm")

print("Program ended.")




    

