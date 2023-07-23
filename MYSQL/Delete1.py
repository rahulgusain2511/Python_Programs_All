import mysql.connector as mysql

mycon = mysql.connect(user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    cursor = mycon.cursor()
    query = "delete from student where rollno=1;"
    cursor.execute(query)
    mycon.commit()
mycon.close()
