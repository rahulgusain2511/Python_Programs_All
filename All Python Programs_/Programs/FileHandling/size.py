#Counting Vowel

def size():
    file = open('Story.txt','r')
    st = file.read()
    b = len(st)
    print("Size is: ",b," bytes")

size()
