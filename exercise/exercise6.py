Talent = int(input("Enter talent: "))
pounds = int(input("Enter pounds:"))
lots = int(input("Enter lots:"))
total_lots = Talent * 20 + pounds * 32 + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams - kilograms * 1000
print (f"the weight is {kilograms} kilograms and  {grams:.2f} grams.")
