#  pickle.dump(data, fileobject)
#  st = pickle.load(fileobject)
import pickle
file = open('binary.dat','wb')
pickle.dump('This is my first binary file.\n',file)
pickle.dump('Hello Python',file)
lst = [1,2,3,4,5]
pickle.dump(lst,file)
file.close()

file = open('binary.dat','rb')
print(pickle.load(file))
print(pickle.load(file))
print(pickle.load(file))
