def changeA(a):
    a = a + 50
    print('A:',a)

def changeList(lst):
    for i in range(len(lst)):
        lst[i] = lst[i] + 10
    print(lst)

def main():
    x = 100
    l = [1,2,3,4,5]
    changeA(x)
    changeList(l)
    print('Hello, I m in main')
    print(x)
    print(l)

if __name__=='__main__':
    main()
