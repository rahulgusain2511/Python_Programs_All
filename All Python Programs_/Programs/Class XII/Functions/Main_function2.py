

def display():
    print("hello i am Display() Function")


def main():
    print("hello i am Main() Function")
    display()
    print("Enter any two numbers: ")
    a = int(input())
    b = int(input())
    c = a + b
    print(c)


'''
main()  # as in python main function is not defined so we need to call
        # it explicitly.
'''
#################################################
''' As every module have a builtin variable '__name__' that contain the
name of the module as '__main__' which designating it be a __main__
module.'''

if __name__ =='__main__':  #so python will check whether the name of the
    main()                 # current module is __main__ or not.
    

