a = 10  #global
def change():
    x = 1  #defined as enclosing
    
    while(x<=5):
        x = x+ 1
        b=1 #defined as local
        #print(c) ERROR c is not defined in (local, enclosing, global & builtin)
        print(a,x,b)

change()
print(a)
