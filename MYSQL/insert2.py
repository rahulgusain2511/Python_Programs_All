import mysql.connector as mysql

mycon = mysql.connect(user='root', passwd='password',database='school')
if not(mycon.is_connected()):
    print('Not connected....')
else:
    rol = int(input('Enter Rollno: '))
    name = input('Enter Name:')
    m =int(input('Enter Marks:'))
    co = input('Enter Course Id:')

    cursor = mycon.cursor()
    query = "INSERT INTO STUDENT(ROLLNO,NAME,MARKS,CID) VALUES({},'{}',{},'{}')".format(rol,name,m,co)
    cursor.execute(query)
    mycon.commit()
mycon.close()
