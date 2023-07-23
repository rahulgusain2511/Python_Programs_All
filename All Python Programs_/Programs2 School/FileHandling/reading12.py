#reading a whole file
def Reading():
    file = open('story.txt')
    st = file.read()
    print('File content: ')
    print(st)

def main():
    Reading()
    
if __name__ == '__main__':
    main()
