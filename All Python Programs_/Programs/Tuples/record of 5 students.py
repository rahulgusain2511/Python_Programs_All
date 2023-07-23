marks = ((55,66,45),(88,78,90),(65,85,100),(10,30,2),(44,35,33),(55,66,68),(88,90,95))
name = ('DIVYANSHU','SIMRAN','VIBHOR','SANDEEP','YASHASVI','SAKSHAM','AYOOSH')
per = [0]*7
t = 0
lmarks = len(marks)
for i in range(lmarks):
    for j in range(3):
        t = t + marks[i][j]
    #end of j
    per[i] = t//3
    t=0
#end of i
######################################
print("Percentage: ")
for i in range(7):
    print(name[i],' :\t',per[i],'%')
######################################
print('Highest Percentage: ')
high = per[0]
pos = 0
for i in range(1,7):
    if per[i]>high:
        high = per[i]
        pos = i
    #end of if
#end of i
print(name[pos],'\t',high)

#####################################
print('Subject wise Highest Marks')
hp, hc, hm = marks[0]
pn, cn, mn = 0,0,0
for i in range(1,7):
    if marks[i][0] > hp:
        hp = marks[i][0]
        pn = i

    if marks[i][1] > hc:
        hc = marks[i][1]
        cn = i

    if marks[i][2] > hm:
        hm = marks[i][2]
        mn = i
#end of i
print('Physics: ',name[pn],hp)
print('Chemistry: ',name[cn],hc)
print('Maths: ',name[mn],hm)




