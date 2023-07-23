word = input('Enter the word: ')
nword=''
for ch in word:
    if ch.isupper():
        nword += ch.lower()
    elif ch.islower():
        nword += ch.upper()
print(nword)
