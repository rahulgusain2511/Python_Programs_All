#Writing a table onto the file.
def table(n):
    file = open('Table.txt','a')
    '''file is a handler which have the ref of Table.txt file
       here the file mode is 'a' ie very time it retain the content
       of the file'''
    for i in range(1,11):
        r = str(i*n)
        s = '\n'+str(n)+'*'+str(i)+'='+r
        file.write(s)
    file.write('\n---------------------')
    file.close()



def main():
    n = int(input('Enter any no for table: '))
    table(n)
    print('Table has been saved...')


if __name__=='__main__':
    main()
