#reading Line by Line
def Reading():
    file = open('story.txt')
    st = ' '
    while st:  #blank string represent false
        st = file.readline()
        print(st,end='')
    print('\nEnd...')
    file.close()

    
def main():
    Reading()

    
if __name__ == '__main__':
    main()
