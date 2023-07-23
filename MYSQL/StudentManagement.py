import mysql.connector as mycon
passw='admin'
def addStudent():
    con = mycon.connect(user='root',passwd='password',database='school')
    if not(con.is_connected()):
        print('Not connected.....')
    else:
        r = int(input('Enter rollno: '))
        n = input('Enter Name: ')
        m = int(input('Enter Marks: '))
        c = input('Enter course Id')
        query = "INSERT INTO STUDENT VALUES({},'{}',{},'{}')".format(r,n,m,c)
        mycur = con.cursor()
        mycur.execute(query)
        con.commit()
        con.close()
        print('Record inserted....\n\n')
#-------------------------------------------------------------------
def searchStudent():
    con = mycon.connect(user='root',passwd='password',database='school')
    if not(con.is_connected()):
        print('Not connected.....')
    else:
        r = int(input('Enter rollno whose record you want to search: '))   
        query="SELECT * FROM STUDENT WHERE ROLLNO={} ".format(r)
        mycur = con.cursor()
        mycur.execute(query)
        data = mycur.fetchone()
        if data != None:
            print(data)
        else:
            print('Record not present......')
        con.commit()
        con.close()
#------------------------------------------------------------------------------------
def deleteStudent():
    global passw
    p = input('\nEnter the password:')
    if p==passw:
        con = mycon.connect(user='root',passwd='password',database='school')
        if not(con.is_connected()):
            print('Not connected.....')
        else:
            r = int(input('Enter rollno whose record you want to Delete: '))
            query1 = "SELECT * FROM STUDENT WHERE ROLLNO={} ".format(r)
            query2="DELETE FROM STUDENT WHERE ROLLNO={}".format(r)
            mycur = con.cursor()
            mycur.execute(query1)
            data = mycur.fetchone()
            if data != None:
                 mycur.execute(query2)
                 print('Record Deleted.....')
            else:
                print('Record not present......')
            con.commit()
            con.close()
    else:
            print('You are not a admin')

#------------------------------------------------------------------------------------
def modifyStudent():
    con = mycon.connect(user='root',passwd='password',database='school')
    if not(con.is_connected()):
        print('Not connected.....')
    else:
        r = int(input('Enter rollno whose record you want to Modify: '))
        query1 = "SELECT * FROM STUDENT WHERE ROLLNO={} ".format(r)
        mycur = con.cursor()
        mycur.execute(query1)
        data = mycur.fetchone()
        if data != None:
            m = int(input('Enter Marks: '))
            c = input('Enter Course Id:')
            query2="UPDATE STUDENT SET CID='{}', MARKS={} WHERE ROLLNO={}".format(c,m,r)
            mycur.execute(query2)
            print('Record Updated....')
        else:
            print('Record not present......')
        con.commit()
        con.close()
def displayStudent():
    con = mycon.connect(host='localhost', user='root', passwd='password',database='school')
    if not(con.is_connected()):
        print('Not connected....')
    else:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM STUDENT')
        data = cursor.fetchall()
    for record in data:
        print(record)
    con.close()

#-----------------------------MAIN---------------------------     
def main():
    while(True):
        print('\n\n1. ADD STUDENT')
        print('2. SEARCH STUDENT')
        print('3. DELETE STUDENT')
        print('4. MODIFY STUDENT')
        print("5. DISPLAY ALL")
        print('6. EXIT')
        ch = int(input('Enter your choice: '))
        if ch==1:
            addStudent()
        elif ch==2:
            searchStudent()
        elif ch==3:
            deleteStudent()
        elif ch==4:
            modifyStudent()
        elif ch==5:
            displayStudent()
        elif ch==6:
            exit()
        else:
            print('WRONG CHOICE ENTERED')
if __name__ == '__main__':
    main()
