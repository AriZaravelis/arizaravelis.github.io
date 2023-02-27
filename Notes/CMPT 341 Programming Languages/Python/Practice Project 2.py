#Project 2
#CMPT 258
#Ari Zaravelis
#Aldona Neziraj


#Print to provide user with the menu
print("""
    1.Enter the instructor ID and I will provide you with the name of the instructor, affiliated department and the location of that department.
    2.Enter the department name and I will provide you with the location, budget and names of all instructors that work for the department.
    3.Insert a record about a new instructor.
    4.Delete a record about an instructor.
    5.Exit
    """)

#Opens instructor.txt
fileInstructor = open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "r")

#Dictionary named instructor
instructor = {}

for line in fileInstructor:
    id,name,dept = line.split(",")
    instructor[id.rstrip()] = name.rstrip()
    instructor[name.rstrip()] = dept.rstrip()
    
    
#Opens department.txt
fileDepartment = open("C:\\Users\\Zarav\\Documents\\Python\\department.txt", "r")


#Dictionary named department
department = {}

for line in fileDepartment:
    dept, location, budget = line.split(",")
    department[dept] = location
    department[location] = budget

#While loop that continues to display the menu until user selects option 5  
while True:
    ans=input("What would you like to do?")

#Displays the following information when user selects option 1
    if ans=="1":
        id=input("\n Enter the instructor ID:")
        if id in instructor:
            print("\nInstructor Name: "+ instructor[id])
            name = instructor[id]
            print("Affiliated department: "+ instructor[name])
            print("Location: "+ department[instructor[name]])
        else:
            print("\nThe ID  does not appear in the file")



#Displays the following information if user selects option 2         
    elif ans=="2":
        dept=input("\n Enter the department name:")
        if dept in department:
            if dept=="CMPT":
                print("Department Budget: $75000")
            elif dept == "MATH":
                print("Department Budget: $55000")
            elif dept == "BIOL":
                print("Department Budget: $60000")
            print("Department Location: "+ department[dept])
            print("Instructors that work for the department: ")
            with open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if dept in line:
                        print(line)
        else:
            print("\nThe department name does not appear in the file")



#Displays the following information if user selects option 3    
    elif ans=="3":
            id=input("\n Enter the instructor id:")
            name=input("\n Enter the instructor name:")
            dept=input("\n Enter the affiliated department name:")
            if(dept not in department):
                print("\nThe department does not exist and hence the instructor record cannot be added to the database\n")
            if(id in instructor):
                print("\nInstructor id already exists\n")
            if(dept in department and id not in instructor ):
                fileInstructor = open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "a+")
                fileInstructor.write("\n" + id+","+name+","+dept)
                fileInstructor.close()
                print ("\n Instructor id: " + id)
                print ("\n Instructor name: " + name)
                print ("\n Affiliated department name: " + dept)



#Displays the following information if user selects option 4
    elif ans=="4":
        id=input("\n Enter the instructor id:")
        if id in instructor:
            name = instructor[id]
            with open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "r") as f:
                lines = f.readlines()
                with open("C:\\Users\\Zarav\\Documents\\Python\\instructor.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != id+","+instructor[id]+","+instructor[name]:
                            f.write(line) 
        else: print("The ID does not appear in the file.")

#Stops while loop and finishes the program     
    elif ans=="5":
        print("\n Goodbye")
        exit()
        break
