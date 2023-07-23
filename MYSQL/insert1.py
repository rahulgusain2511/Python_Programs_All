import mysql.connector as mysql

mycon = mysql.connect(user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    cursor = mycon.cursor()
    query = "INSERT INTO STUDENT VALUES(8,'ARPIT',77,'COO5')"
    cursor.execute(query)
    mycon.commit()
mycon.close()
