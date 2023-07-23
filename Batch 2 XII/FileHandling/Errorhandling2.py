c=0
a =  int(input("Enter any first number: "))
b =  int(input("Enter any second number: "))

try:
    c = a / b
    print("Everything went well")

except:
    print("Number cannot be divided by zero")

finally:
    print('Division',c)

print('Bye - 2')


