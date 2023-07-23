#Q14 Area of different figs
print("\t\t1. Area of SQUARE")
print("\t\t2. Area of RECTANGLE")
print("\t\t3. Area of CIRCLE")
print("Enter your choice: ")
ch = int(input())

if ch==1:
    s = int(input("Enter the side of a square: "))
    print('Area of Square: ',(s*s))
elif ch==2:
    l = int(input("Enter length: "))
    b = int(input("Enter Width: "))
    print("Area of Rectangle: ",(l*b))
elif ch==3:
    r = int(input("Enter Radius: "))
    print("Area of Circle: ",3.14*r*r)
else:
    print("Wrong choice entered...")
#end
