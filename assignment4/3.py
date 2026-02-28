cities=[]

print("enter the names of five cities")

for i in range(5):
    name = input(f"Enter city {i+1}: ")
    cities.append(name)
print("\nYou entered the following cities:")

for city in cities:
    print(city)