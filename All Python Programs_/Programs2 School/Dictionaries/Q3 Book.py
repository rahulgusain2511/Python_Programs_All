month={'JAN':31, 'FEB':28, 'MAR':31,
       'APR':30, 'MAY':31, 'JUN':30,
       'JUL':31, 'AUG':31,'SEP':30,
       'OCT':31,'NOV':30,'DEC':31}
#1
m = input("Enter the month name: ")
n = month.get(m,'Invalid Value')
print(m,n,sep=':')
#2
lst = list(month.keys())
lst.sort()
print("Sorted month: ")
print(lst)
#3
for k in month:
    if month[k]==31:
        print(k)
#4
lst = list(month.values())
lst.s
    

