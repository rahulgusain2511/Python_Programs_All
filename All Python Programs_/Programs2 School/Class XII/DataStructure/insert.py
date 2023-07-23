# A = [10, 20, 30, 60, 90]
# insert 50
# A = [10, 20, 30, 50 60, 90]
def findIndex(lst, num):
    pos=0
    l = len(lst)
    if num <= lst[0]:
        return pos
    for i in range(l-1):
        if lst[i] < num <= lst[i+1]:
            pos = i+1
            return pos
    return l
    
def insert(lst, num, pos):
    lst.append(None)
    l = len(lst)
    for i in range(l-1,pos,-1):
        lst[i] = lst[i-1]
    lst[pos] = num
def main():
    lst=[10,20,30,70,100]
    print(lst)
    n = int(input('Enter any no: '))
    pos = findIndex(lst, n)
    insert(lst, n, pos)
    print(lst)

if __name__== '__main__':
    main()
