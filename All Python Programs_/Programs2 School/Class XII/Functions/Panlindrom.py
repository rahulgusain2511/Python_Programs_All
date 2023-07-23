def isPalindrome(num):
    rev=0
    save = num
    while(num>0):
        r = num%10
        rev = rev*10 + r
        num //=10
    if rev==save:
        print(save," is Palindrome")
    else:
        print(save," is not Palindrome")


#isPalindrome(123)
