
front, rear = -1,-1 # Queue is empty
def Enqueue(q, n):
    global front, rear
    if rear==9:
        print('Queue is overflow....')
    elif front==-1:
        front, rear = 0,0
        q.append(n)
    else:
        rear = rear + 1
        q.append(n)
    print('Value added....')

'''
q.append(n)
front = 0
rear = len(q) - 1
--------------------
q.append(n)
if len(q) == 1:
    front,rear = 0,0
else:
    rear = len(q) - 1
'''
def Dequeue(q):
    global front, rear
    if front == -1:        #len(q) == 0
        print('Queue is underflow...')
    else:
        n = q.pop(front)
        if len(q) == 0:
            front, rear = -1, -1
        else:
            rear = len(q) - 1
        print(n,' is deleted...')

def Peek(q):
    global front, rear
    if front == -1:
        print('Queue IS UNDERFLOW')
    else:
        t = q[front]
        print('First Element: ',t)

def Display(q):
    global front, rear
    if front == -1:
        print('QUEUE IS UNDERFLOW')
    else:
        i = front
        while(i<=rear):
            print(q[i],end='->')
            i = i+1       
    
    
def main():
    queue = []
    while True:
        print('\n1. Enqueue')
        print('2. Dequeue')
        print('3. Peek')
        print('4. Display')
        ch = int(input('ENTER YOUR CHOICE: '))
        if ch==1:
            n = int(input('Enter any number: '))
            Enqueue(queue, n)
        elif ch==2:
            Dequeue(queue)
        elif ch==3:
            Peek(queue)
        elif ch==4:
            Display(queue)
        else:
            print('Incorrect Option')


if __name__ == '__main__':
    main()

















