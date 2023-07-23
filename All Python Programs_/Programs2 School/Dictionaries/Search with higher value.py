comp = {'Mohit':5, 'Mayank':1, 'Monu':3, 'Meenu':6, 'Sonu':9}
m=0
hero=''
for key in comp:
    if comp[key]>m:
        m = comp[key]
        hero = key
print(hero,":",m)
