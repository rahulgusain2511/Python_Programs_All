game = {}
n = int(input('enter the no. of students: '))
for i in range(n):
    key = input('Enter student name: ')
    value = input('Enter number of wins: ')
    game[key] = value
print(game)
 
