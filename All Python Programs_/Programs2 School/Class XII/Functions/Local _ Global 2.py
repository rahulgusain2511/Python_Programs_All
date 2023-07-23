x = 10  #Global
def change():
    x = 50   #local
    print('Change Function: ')
    print('Local X: ',x)  #50
    print('Global X: ',x) #50
    print('Global X: ',x)

change()
print('Main: ')
print('Global X: ',x)
