import pickle
file = open('binary1.dat','wb')
for i in range(5):
    name = input('Enter name:')
    r = input('Enter Rollno:')
    pickle.dump(r,file)
    pickle.dump(name,file)
file.close()
print('End')
-