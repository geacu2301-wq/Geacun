first_number = True
while True:
    n= (input(" enter a number"))
    if n == " ":
        break
    if first_number:
        largest_number=n
        smallest_number=n
        first_number= False        
    else:
        if n> largest_number:
            largest_number=n
        if n< smallest_number:
            smallest_number=n
            print ("largest number is", largest_number)
            print ("smallest number is", smallest_number)
    

