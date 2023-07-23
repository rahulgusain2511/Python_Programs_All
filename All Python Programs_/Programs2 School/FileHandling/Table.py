#Writing a table onto the file.
def table(n):
    file = open('Table.txt','w')
    '''file is a handler which have the ref of Table.txt file
       here the file mode is w ie very time it overwrite the content
       of the file'''
    for i in range(1,11):
        r = str(i*n)
        s = str(n)+'*'+str(i)+'='+r+'\n'
        file.write(s)



def main():
    n = int(input('Enter any no for table: '))
    table(n)
    print('Table has been saved...')


if __name__=='__main__':
    main()
