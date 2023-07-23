a = 10  #global
def change():
    global a
    a = 5 #hides the global a
    x = a + 10  #local
    print(a,x)

change()
print(a)
