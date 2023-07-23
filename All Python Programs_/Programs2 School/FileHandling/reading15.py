#reading Line by Line
def Reading():
    file = open('story.txt')
    st = file.readlines()
    print(st)
    print("\n\nNo. of Lines: ",len(st))
    file.close()

    
def main():
    Reading()

    
if __name__ == '__main__':
    main()
