import mysql.connector as mysql

mycon = mysql.connect(user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    r = int(input('Enter rollno:'))
    m = int(input('Enter Marks:'))
    data = (m,r)
    cursor = mycon.cursor()
    query = "UPDATE STUDENT SET MARKS= %s where rollno=%s"
    cursor.execute(query,data)
    mycon.commit()
mycon.close()
