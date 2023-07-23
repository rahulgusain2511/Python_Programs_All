d = {'Rohan':{'rollno':1, 'marks':67, 'age':13},
     'Mayank':{'rollno':2, 'marks':690, 'age':15},
     'Simran':{'rollno':3, 'marks':89, 'age':16},
     'Divyanshu':{'rollno':4, 'marks':77, 'age':15}}
#d = eval(input("Enter the details: "))
name = input('Enter the name whose record you want to search: ')

flag=False
for key in d:
    if name == key:
        print(d[key])
        flag=True
        break;
if not(flag):
    print('Student not present')
print('End')
