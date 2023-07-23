def sum(*n):  #*n represent varible length for the argument
    s = 0
    for i in n:            #internally n represent values as a tuple.
        s = s + i
    print("Sum: ",s)

sum()  #actual argument: 0
sum(2,3)  #actual argument: 2
sum(4,5,6,7,8)  #actual argument: 5
