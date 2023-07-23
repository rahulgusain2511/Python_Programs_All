comp = {'Mohit':5, 'Mayank':1, 'Monu':3, 'Meenu':6, 'Sonu':9, 'Roshan':10, 'James':4, 'Zeba':2, 'Atmos':4}
flag=0
name = input("Enter the Name to delete: ")
for key in comp:
    if key == name:
        flag=1
        break;
if flag==1:
    del comp[name]
else:
    print("Record not found")

print(comp)
