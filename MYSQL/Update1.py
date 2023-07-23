import mysql.connector as mysql

mycon = mysql.connect(user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    cursor = mycon.cursor()
    query = "UPDATE STUDENT SET MARKS= MARKS + 2"
    cursor.execute(query)
    mycon.commit()
mycon.close()
