#reading a whole file
def Reading():
    file = open('story.txt')
    st = file.read(1)
    print(st)
    st = file.read(1)
    print(st)

def main():
    Reading()

    
if __name__ == '__main__':
    main()
