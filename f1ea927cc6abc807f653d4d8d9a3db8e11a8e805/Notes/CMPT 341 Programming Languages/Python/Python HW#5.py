import mysql.connector
        
try:
    mydb = mysql.connector.connect(
        user='root',
        password='7698frza'
    )
    
    mycursor = mydb.cursor()
    #mycursor.execute("create database mydb;")
    mycursor.execute("use mydb;")

    mycursor.execute("create table instructor (id varchar(4), name varchar(20), dept_name varchar(20)")
    
    mycursor.execute("insert into instructor values('1', 'Tian Tian', 'CS');")
    mycursor.execute("insert into instructor values('2', 'Marvin Bishop', 'Math');")
    mycursor.execute("insert into instructor values('3', 'Kashifuddin Qazi', 'CS');")
    mycursor.execute("insert into instructor values('4', 'Sr.Joan', 'Math');")
    
    mydb.commit()
    
    department = input("Enter department name(Press -1 when your finished): ")
    
    mydb.execute("SELECT name FROM instructor WHERE dept_name = '{}'".format(department))
    myresult = mydb.fetchall()
    if len(myresult) == 0:
        print("\nNo instructors found")
    else:
        for i in myresult:
            print(i[0])

except:
    print("\nCannot access database")
#mydb.close()
