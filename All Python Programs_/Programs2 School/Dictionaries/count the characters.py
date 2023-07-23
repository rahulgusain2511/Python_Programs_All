text='abracadabraaabbccrr'
counts={}
for  ch in text:
    if ch not in counts:
        counts[ch]=0
    counts[ch] = counts[ch]+1
print(counts)

