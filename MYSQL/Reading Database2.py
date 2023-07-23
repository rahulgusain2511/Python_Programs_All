import mysql.connector as mysql

mycon = mysql.connect(user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    cursor = mycon.cursor()
    cursor.execute('SELECT * FROM STUDENT')
    print('Before Fetch: ',cursor.rowcount)
    record = cursor.fetchone()
    while record:
        count = cursor.rowcount
        print(count,':',record)
        record = cursor.fetchone()
mycon.close()
