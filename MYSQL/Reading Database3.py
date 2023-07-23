import mysql.connector as mysql

mycon = mysql.connect(host='localhost', user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    cursor = mycon.cursor()
    cursor.execute('SELECT * FROM STUDENT')
    record = cursor.fetchmany(2)
    print(record)
    record = cursor.fetchmany(4)
    print(record)
mycon.close()

