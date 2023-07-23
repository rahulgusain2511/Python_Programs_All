
def findIndex(lst, num):
   # flag = -1
    for i in range(len(lst)):
        if num==lst[i]:
            return i
    return -1
        
def main():
    lst=[10,20,30,70,100]
    print(lst)
    n = int(input('Enter any no: '))
    pos = findIndex(lst, n)
    if pos >= 0:
        del(lst[pos])
    else:
        print('No. not present')
    print(lst)

if __name__== '__main__':
    main()


    
