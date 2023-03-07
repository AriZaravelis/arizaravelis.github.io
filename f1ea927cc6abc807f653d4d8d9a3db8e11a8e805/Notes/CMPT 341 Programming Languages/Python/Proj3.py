import mysql.connector

def import_data(): # Reads instructor and department .txt files and creates their respective MySQL tables
    try:
        f = open("C:\\Users\\Zarav\\Documents\\Python\\department.txt", "r")
        c.execute("""create table department(dept_name varchar(20),
        location varchar(20), budget numeric(8,2), primary key (dept_name));""")
        for i in f:
            line = [atr.strip() for atr in i.split(',')]
            c.execute("""insert into department values ('{}', '{}', '{}');""".format(line[0], line[1], line[2]))
        f.close()
        f = open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "r")
        c.execute("""create table instructor(id varchar(4), name varchar(20), dept_name varchar(20), primary key(id), foreign key(dept_name) references department(dept_name));""")
        for i in f:
            line = [atr.strip() for atr in i.split(',')]
            c.execute("""insert into instructor values ('{}', '{}', '{}');""".format(line[0], line[1], line[2]))
        f.close()
        connect.commit()
        print("Created tables")
    except:
        print("Loaded tables")

def print_menu(): # Prints the main menu and return the user's input option
    print("\nMain Menu:")
    print("1. Enter the instructor ID and I will provide you with the name of the instructor, affiliated department and the location of that department.")
    print("2. Enter the department name and I will provide you with the location, budget and names of all instructors that work for the department.")
    print("3. Insert a record about a new instructor.")
    print("4. Delete a record about an instructor")
    print("5. Exit")
    return input("Enter an option: ")

try:
    connect = mysql.connector.connect(user = 'root', password = '7698frza') # Establish connection
    c = connect.cursor() # Makes cursor object
    try: # Try to create database
        c.execute("""create database university;""")
        print("Creating database university...")
    except: # If database cannot be created, then it already exists
        print("Loaded database university")
    c.execute("""use university;""") # Use the database
    import_data() # imports data from .txt files
    option = print_menu() # Prints the main menu
    while not option == "5": # Loop runs until user enters "5"
        if option == "1": # Enter instructor ID and instructor info will appear
            ID = input("Enter the instructor's ID: ")
            try:
                c.execute("""select name, dept_name, location from department natural join instructor where id = '{}'""".format(ID))
            except:
                print("\n" + ID, "is not a valid entry.")
                option = print_menu()
                continue
            result = c.fetchone()

            if result is None:
                print("\nThe ID does not appear in the database.")
            else:
                print("\nMatch Found:")
                print("Name:", result[0])
                print("Department:", result[1])
                print("Location:", result[2])
        elif option == "2": # Enter department name and both department info and instructors in that department will appear
            dept = input("Enter the department name: ")
            try:
                c.execute("""select name from instructor where dept_name = '{}'""".format(dept))
                instructors = c.fetchall()
                c.execute("""select location, budget from department where dept_name = '{}'""".format(dept))
                location_budget = c.fetchone()
            except:
                print("\n" + dept, "is not a valid entry.")
                option = print_menu()
                continue
            if location_budget is None:
                print("\nThe department name does not appear in the database.")
            else:
                print("\n" + dept, "department:")
                print("Location:", location_budget[0])
                print("Budget:", location_budget[1])
                if instructors is None:
                    print("\nThere are no instructors in the", dept, "department.")
                else:
                    print("\nInstructors in the", dept, "department:")
                    for i in instructors:
                        print(i[0])
        elif option == "3": # Enter information about new instructor and adds it to the database
            ID = input("Enter the instructor id: ")
            name = input("Enter the instructor name: ")
            dept = input("Enter the affiliated department name: ")
            try:
                c.execute("""select dept_name from department;""")
            except:
                print("\n" + dept, "is not a valid entry.")
                option = print_menu()
                continue
            temp = c.fetchall()
            departments = []
            for i in temp:
                departments.append(i[0])
            try:
                c.execute("""select id from instructor;""")
            except:
                print("\n" + ID, "is not a valid entry.")
                option = print_menu()
                continue
            temp = c.fetchall()
            IDS = []
            for i in temp:
                IDS.append(i[0])
            if dept not in departments:
                print("\nThe department does not exist and hence the instructor record cannot be added to the database")
            elif ID in IDS:
                print("\nInstructor id already exists in the database.")
            else:
                c.execute("""insert into instructor values('{}', '{}', '{}');""".format(ID, name, dept))
                connect.commit()
                print("\nValues have been recorded.")
        elif option == "4": # Enter an ID and the instructor will be removed from the database
            ID = input("Enter the instructor id: ")
            try:
                c.execute("""select id from instructor;""")
            except:
                print("\n" + ID, "is not a valid entry.")
                option = print_menu()
                continue
            temp = c.fetchall()
            IDS = []
            for i in temp:
                IDS.append(i[0])
            if ID not in IDS:
                print("\nThe ID does not appear in the database.")
            else:
                c.execute("""delete from instructor where id = '{}'""".format(ID))
                connect.commit()
                print("\nRecord has been deleted.")
        else: # User entered an option that is excluded from the main menu
            print("\n" + option, "is an invalid entry.")
        option = print_menu() # Function call; user enters option from main menu before the next iteration begins
    print("You have exited the program.") # User has exited the program as soon as the program goes out of the while loop
    c.close() # Closes the connection

except: # If a connection cannot be established, then print a message saying so
    print("Cannot connect to MySQL")
