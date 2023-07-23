n = int(input("How many students: "))
comp = {}  # comp = dict()
for i in range(n):
    name = input("Enter the name of a student: ")
    win = int(input("Number of Competitions won: "))
    comp[name] = win
print(comp)
for key in comp:
    print(key,":",comp[key])
