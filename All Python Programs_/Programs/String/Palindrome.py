st1 = ''
st2 = input("enter any word: ")
st1 = st2[::-1]
if st2==st1:
    print("Palindrome")
else:
    print("Not a Palindrome")
