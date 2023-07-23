
unit = int(input("Enter the unit: "))
if( 0 <= unit <= 100):
    amt = unit*2.65
elif(100 < unit <= 200):
    amt = 265 + (unit-100)*3.45
elif(200 < unit <= 400):
    amt = 265 + 345 + (unit-200)*4.7
else:
    amt = 265+ 345 + 940 + (unit-400)*5.4
print("Bill: ",amt)
