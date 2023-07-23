n = int(input("Enter the number of teams: "))
team={}
for i in range(n):
    key=input("Enter the team name: ")
    w= int(input("enter the wins: "))
    l = int(input("enter the lost: "))
    team[key] = [w,l]
print(team)
t1 = input("Enter the team name: ")
if t1 in team:
    p = (team[t1][0]/(team[t1][0] + team[t1][1] ))*100
    print("Winning %: ",p)
else:
    print("Wrong team entered...")
win=list()
for k in team:
    win.append(team[k][0])
print("Winning list: ",win)
