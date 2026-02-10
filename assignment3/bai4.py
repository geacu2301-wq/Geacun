import random
number = random.randint(1, 10)   
guess = 0
while guess != number:
    guess = int(input("Enter your number between 1 and 10: "))
    if guess > number:
        print("Too high")
    elif guess < number:
        print("Too low")
    else:
        print("Correct")
  

        