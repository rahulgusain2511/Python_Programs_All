#Q22
netamt, dis = 0.0, 0.0
amt = int(input("Enter the purchasing amount: "))
if amt>=0 and amt<=2000:
    dis = amt*0.05
elif amt>2000 and amt<=5000:
    dis = 100 + (amt-2000)*0.1
elif amt>5000 and amt<=10000:
    dis = 100 + 300 + (amt-5000)*0.15
elif amt>10000:
    dis = 100 + 300 + 750 + (amt-10000)*0.2
else:
    print("Wrong value entered...")
netamt = amt-dis
print("Amount: ",amt)
print("Discount: ",dis)
print("Net Payable: ",netamt)
    
