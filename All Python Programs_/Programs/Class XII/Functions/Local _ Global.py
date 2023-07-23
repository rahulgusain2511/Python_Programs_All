x = 10  #Global

def change():
    y = x + 10   # y is local
    print('y: ',y)

change()

#print('y: ',y)  ERROR
print('x: ',x)
#print(z)  ERROR variables always declared before use
#z = 100    
