#Q21
amt = 0
unit = int(input("Enter the unit consumed: "))
if unit>=0 and unit<=100:
    amt = 200 + unit*3
elif unit>100 and unit<=200:
    amt = 200 + 300 + (unit-100)*3.5
elif unit>200:
    amt = 200 + 300 + 350 + (unit-200)*5
else:
    print("Wrong number of units entered...")
print("Total Amount: ",amt)
