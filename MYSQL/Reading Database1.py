import mysql.connector as mysql

mycon = mysql.connect(host='localhost', user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    cursor = mycon.cursor()
    cursor.execute('SELECT * FROM STUDENT')
    data = cursor.fetchall()
    for record in data:
        print(record)
    mycon.close()
