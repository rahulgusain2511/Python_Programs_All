
front = rear = -1

#--------push
def enqueue(qu, n):
    global front, rear
    qu.append(n)
    if front==-1:
        front = rear = 0
    else:
        rear = len(qu)-1
        
    print('no. pushed...')
#---------pop
def dequeue(qu):
    global front, rear
    if(len(qu)==0):   #front==-1
        print('Queue is underflow')
    else:
        n = qu.pop(0)
        if len(qu)==0:
            front = rear = -1
        print(n,' is deleted...')
#---------display
def display(qu):
    global front, rear
    if(len(qu)==0):
        print('Queue is underflow')
    else:
        for i in range(front,len(qu)):
            print(qu[i])

        
def main():
    queue = []
    while True:
        print("1. enqueue")
        print("2. dequeue")
        print("3. DISPLAY")
        print("4. EXIT")
        ch = int(input('Enter your choice: '))
        if ch==1:
            n = int(input('Enter any no: '))
            enqueue(queue, n)
        elif ch==2:
            dequeue(queue)
        elif ch==3:
            display(queue)
        else:
            exit(0)

if __name__ == '__main__':
    main()

        
