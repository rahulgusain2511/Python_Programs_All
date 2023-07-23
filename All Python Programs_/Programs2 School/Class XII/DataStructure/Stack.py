
top = -1 # stack is empty

def PUSH(st, n):  #insertion in a stack
    global top
    if top==9:
        print('STACK IS OVERFLOW')
    else:
        st.append(n)  
        top = top + 1   # top = len(st) + 1
        #st[top] = n   [0 for i in range(10)]    

def POP(st):
    global top
    if top == -1:  
        print('STACK IS UNDERFLOW')
    else:
        t = st.pop()
        top = top - 1  #top = len(st) - 1
        print(t,' Deleted....')

def PEEK(st):
    global top
    if top == -1:
        print('STACK IS UNDERFLOW')
    else:
        t = st[top]
        print('TOP ELEMENT: ',t)

def DISPLAY(st):
    global top
    if top == -1:
        print('STACK I UNDERFLOW')
    else:
        i = top
        while(i>=0):
            print(st[i])
            i = i-1       
    
    
def main():
    stack = []
    while True:
        print('\n1. PUSH')
        print('2. POP')
        print('3. PEEK')
        print('4. DISPLAY')
        ch = int(input('ENTER YOUR CHOICE: '))
        if ch==1:
            n = int(input('Enter any number: '))
            PUSH(stack, n)
        elif ch==2:
            POP(stack)
        elif ch==3:
            PEEK(stack)
        elif ch==4:
            DISPLAY(stack)
        else:
            print('Incorrect Option')


if __name__ == '__main__':
    main()

















