def Write1(a, b, c):
    print(a,b,c, sep=':')

def Write2(a, b, c=100):
    print(a,b,c, sep=':')

#def Write3(a=10, b, c): ERROR default argument never follows non-default argu.
def Write3(a=3,b=2,c=1):
    print(a,b,c, sep=':')


Write1(10,20,30)
#Write1(100,200) ERROR required one more argument

Write2(100,200)
Write2(1,2,3)

Write3()
Write3(10)
Write3(150,250)
Write3(0,0,0)




