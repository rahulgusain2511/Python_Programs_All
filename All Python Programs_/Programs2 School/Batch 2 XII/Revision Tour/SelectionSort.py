lst = eval(input('Enter the list: '))
leng = len(lst)
for i in range(leng):
    small = lst[i]
    pos = i
    for j in range(i+1,leng):
        if lst[j]<small:
            small = lst[j]
            pos = j
    lst[i], lst[pos] = small, lst[i]
    print('Pass: ',i+1,'\n',lst)
