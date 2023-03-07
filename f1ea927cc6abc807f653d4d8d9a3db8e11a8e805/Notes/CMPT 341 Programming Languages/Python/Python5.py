import mysql.connector

connect = mysql.connector.connect(user= 'root', password='7698frza')
c = connect.cursor()
c.execute("""use uni""")
    
'''
c.execute(("""create database uni;"""))
c.execute("""use uni""")
c.execute("""create table instructor(id varchar(4), name varchar(20), dept_name varchar(20));""")
c.execute("""insert into instructor values ('1', 'Tian Tian', 'CS');""")
c.execute("""insert into instructor values ('2', 'Marvin Bishop', 'Math');""")
c.execute("""insert into instructor values ('3', 'Kashifuddin Qazi', 'CS');""")
c.execute("""insert into instructor values ('4', 'Sr. Joan', 'Math');""")
connect.commit()
'''

while True:
    dept = input("Enter department name(Press -1 when finished): ")
    c.execute("""select name from instructor where dept_name = '{}'""".format(dept))
    result = c.fetchall()
    if dept == "-1":
        break
    elif len(result) == 0:
        print("No instructors found.")
    else:
        for i in result:
            print(i[0])
connect.close()
