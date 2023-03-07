import mysql.connector

connect = mysql.connector.connect(user= 'root', password='7698frza')
c = connect.cursor()



c.execute(("""create database university;"""))
c.execute("""use university""")

f = open("C:\\Users\\Zarav\\Documents\\Python\\department.txt", "r")
c.execute("""create table department(dept_name varchar(20), location varchar(20), budget numeric(8,2), primary key (dept_name));""")
for i in f:
    line = [atr.strip() for atr in i.split(',')]
    c.execute("""insert into department values ('{}', '{}', '{}');""".format(line[0], line[1], line[2]))
    f.close()
    connect.commit()
f = open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "r")
c.execute("""create table instructor(id varchar(4), name varchar(20), dept_name varchar(20), primary key(id), foreign key(dept_name) references department(dept_name));""")
for i in f:
    line = [atr.strip() for atr in i.split(',')]
    c.execute("""insert into instructor values ('{}', '{}', '{}');""".format(line[0], line[1], line[2]))
    f.close()
    connect.commit()


print("""
    1.Enter the instructor ID and I will provide you with the name of the instructor, affiliated department and the location of that department.
    2.Enter the department name and I will provide you with the location, budget and names of all instructors that work for the department.
    3.Insert a record about a new instructor.
    4.Delete a record about an instructor.
    5.Exit
    """)


while True:
    ans=input("What would you like to do?")


    
#Displays the following information when user selects option 1
    if ans=="1":
        id_input = input("Enter instructor id: ")

        print("Instructor Name: ")
        c.execute("""select name from instructor where id = '{}'""".format(id_input))
        result = c.fetchall()
        if len(result) == 0:
            print("No instructors found.")
        else:
            for i in result:
                print(i[0])

                
        print("Affiliated Department: ")
        c.execute("""select dept_name from instructor where id = '{}'""".format(id_input))
        result = c.fetchall()
        if len(result) == 0:
            print("No instructors found.")
        else:
            for i in result:
                dept = (i[0])
                print (dept)

        print("Location of Department: ")
        c.execute("""select location from department where dept_name = '{}'""".format(dept))
        result = c.fetchall()
        if len(result) == 0:
            print("No instructors found.")
        else:
            for i in result:
                print(i[0])



#Displays the following information if user selects option 2               
    elif ans=="2":
        dept_name_input = input("Enter department name: ")

        print("Location: ")
        c.execute("""select location from department where dept_name = '{}'""".format(dept_name_input))
        result = c.fetchall()
        if len(result) == 0:
            print("No instructors found.")
        else:
            for i in result:
                print(i[0])


        print("Budget: ")
        c.execute("""select budget from department where dept_name = '{}'""".format(dept_name_input))
        result = c.fetchall()
        if len(result) == 0:
            print("No instructors found.")
        else:
            for i in result:
                print(i[0])


        print("Names of all instructors that work for the department: ")
        c.execute("""select name from instructor where dept_name = '{}'""".format(dept_name_input))
        result = c.fetchall()
        if len(result) == 0:
            print("No instructors found.")
        else:
            for i in result:
                print(i[0])

                

#Displays the following information if user selects option 3    
    elif ans=="3":
        id_input = input("Enter the instructor id: ")
        name_input = input("Enter the instructor name: ")
        dept_name_input = input("Enter the affiliated department name: ")

        if(dept_name_input not in 'department'):
            print("The department does not exist and hence the instructor record cannot be added to the database")
        if(id_input in 'instructor'):
            print("Instructor id already exists")
        if(dept_name_input in 'department' and id_input not in 'instructor'):
            c.execute("insert into instructor(id, name, dept_name) values(%s,%s,%s)",
                      (id_input, name_input, dept_name_input))
            connect.commit()

            

#Displays the following information if user selects option 4
    elif ans=="4":
        id_input=input("\n Enter the instructor id:")
        if id_input in 'instructor':
            c.execute("delete from instructor where id = 'id_input'")
            connect.commit()
            print(mycursor.rowcount, "record(s) deleted")
        else: print("The ID does not appear in the file.")



#Stops while loop and finishes the program     
    elif ans=="5":
        print("\n Goodbye")
        exit()
        break







