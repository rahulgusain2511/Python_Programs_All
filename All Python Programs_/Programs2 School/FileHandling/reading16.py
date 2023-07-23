#reading Line by Line
def Reading():
    file = open('story.txt')
    st = file.readlines()
    for s in st:
        print(s,end='')
    file.close()

    
def main():
    Reading()

    
if __name__ == '__main__':
    main()
