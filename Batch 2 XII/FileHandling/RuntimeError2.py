import pickle
file = open('binary1.dat','rb')
st = ' '
#while st:
st = pickle.load(file)
print(st)
print('file ends')
file.close()
