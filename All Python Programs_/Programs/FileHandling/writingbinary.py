#Writing on a binary file
import pickle
import sys
def writing():
    file = open("binary.dat",'ab')
    st = input('Enter any thing: ')
    pickle.dump(st, file)
    file.close()
    

writing()
sys.stdout.write("hello")
sys.stderr.write('BYE')
