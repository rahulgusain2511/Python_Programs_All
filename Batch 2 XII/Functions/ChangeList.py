def ChangeList(lst):
    l = len(lst)
    for i in range(l):
        if lst[i]%5==0:
            lst[i] = lst[i]*5
    return lst

l = eval(input('Enter any list: '))
print(ChangeList(l))
