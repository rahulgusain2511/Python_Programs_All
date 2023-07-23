def calculator(a, b):   #formal argument / formal parameters
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c,d,e,f    #multiple values are returning..

x = calculator(10,5) #actual argument
print(type(x))
print(x)
