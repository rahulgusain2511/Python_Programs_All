def to_string(n,base):
   conver_tString = "01"#23456789ABCDEF"
   if n < base:
      return conver_tString[n]
   else:
      return to_string(n//base,base) + conver_tString[n % base]

print(to_string(3,2))
i=0
st = 'hello\0'
while(st[i]!= '\0'):
    print(st[i])
    i += 1
