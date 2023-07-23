import pickle
file = open('binary1.dat','rb')
try:
    while True:
        st = pickle.load(file)
        print(st)
except EOFError:
    print('file ends')
finally:
    file.close()

#load function is used to read data from the file. it take one
#argument ie file object.
'''
and to read whole file we need to use loop. But load function throws an
exception ie EOFERROR.
so we need to handle this error through try - except block.
'''

