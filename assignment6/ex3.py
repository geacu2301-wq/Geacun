names = set()
while True:
    name= input()
    if name == "":
        break
    if name in names:
        print("existing name")
    else:
        names.add(name)
    print ("new name")
    for name in names:
        print(name)
        
        
    