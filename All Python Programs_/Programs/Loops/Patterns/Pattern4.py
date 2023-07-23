'''
@ 
@ @
@ @ @ 
@ @ @ @
'''
#here columns are varying according to the number of the row
#so, two LOOP is required one is for rows and other for column.

for i in range(1,5):  #rows
    for j in range(1,i+1): #columns
        print('@',end=' ')
    print()
'''
i = 1   range(1,2) : [1]
i = 2   range(1,3) : [1, 2]
i = 3   range(1,4) : [1, 2, 3]
i = 4   range(1,5) : [1, 2, 3, 4]
'''
