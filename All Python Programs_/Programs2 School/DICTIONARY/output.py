'''aDict = {'Bhavna':1, 'Richard':2, 'Firoz':10, 'Abdul':20}
temp = 0
for value in aDict.values():
    temp = temp+ value
print(temp)
'''

aDict = {'Bhavna':1, 'Richard':2, 'Firoz':10, 'Abdul':20}
temp = ''
for k in aDict:
    if temp < k:
        temp = k
print(temp)
