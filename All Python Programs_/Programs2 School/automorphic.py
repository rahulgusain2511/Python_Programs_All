#automorphic
for i in range(1,1001):
    n = str(i)
    digit = len(n)
    n = int(n)
    sq = n*n
    last = sq%10**digit
    if(last == n):
        print(n,"is automorphic")
        print()
else:  #loop
    print("Ends")
