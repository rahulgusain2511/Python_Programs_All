import mysql.connector as mysql

mycon = mysql.connect(host='localhost', user='root', passwd='password',database='school')
if mycon.is_connected():
    print('Successful connected...')
else:
    print('Not connected....')
