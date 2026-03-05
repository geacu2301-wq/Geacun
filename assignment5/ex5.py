import random
points = int(input("Enter your point: "))
inside = 0
count = 0
while count < points:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 < 1:
        inside += 1
    count += 1
pi = 4 * inside / points
print("The estimation of pi is:", pi)
    