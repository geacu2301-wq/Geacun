Season = ("Spring", "summer", "autumn", "winter")
months= int(input("Enter month from 1 to 12:"))
if months in [3,4,5]:
    print(Season[0])
elif months in [6,7,8]:
    print(Season[1])
elif months in [9,10,11]:
    print(Season[2])
else:
    print(Season[3])