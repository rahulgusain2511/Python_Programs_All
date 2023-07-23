l=eval(input('enter the list'))
n=int(input('enter the number to check'))
count=0
for i in range(len(l)):
    if l[i]==n:
        count+=1
print('Frequency:',count)
          
