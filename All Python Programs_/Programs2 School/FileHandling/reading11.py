#reading a whole file
def Reading():
    file = open('story.txt')
    st = 0
    while st:  #blank string represent false
        st = file.read(1)
        print(st,end='')
    print('\nEnd...')
    file.close()

    
def main():
    Reading()

    
if __name__ == '__main__':
    main()
