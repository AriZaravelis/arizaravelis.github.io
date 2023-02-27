# Project 1 
# CMPT 258 

# Ari Zaravelis
# Aldona Neziraj 


# List of instructors ID
instructorID=["1001", "1002", "1003", "1004", "1005", "1006"]

# List of  Instructors names 
instructorName=["Robert Smith", "Natasha Anderson", "James Nassimi", "Guiling Wei", "Mary Harnett", "David Ochs",]

#List of the instructors departments 
instructorDept=["CMPT", "MATH", "BIOL", "CMPT", "BIOL", "CMPT"]

departmentName=["CMPT", "MATH", "BIOL"]

departmentLocation=["RLC", "RLC", "LEO"]

departmentBudget=["75000", "55000", "60000"]

# Print to provide user with the menu 
print("""
    1.Enter the instructor ID and I will provide you with the name of the instructor, affiliated department and the location of that department.
    2.Enter the department name and I will provide you with the location, budget and names of all instructors that work for the department.
    3.Insert a record about a new instructor.
    4.Exit
    """)

#While loop that displays the menu until user selects option 4

while True:
    ans=input("What would you like to do?")
# Displays the following information when user selects option 1
    if ans=="1":
        id=input("\n Enter the instructor ID:")
        if id in instructorID:
            idIndex=instructorID.index(id)
            name=instructorName[idIndex]
            dept=instructorDept[idIndex]
            deptIndex=departmentName.index(dept)
            location=departmentLocation[deptIndex]
            print("\nInstructor Name: "+name)
            print("Affiliated department: "+dept)
            print("Location: "+location)
        else:
            print("\nThe department name does not appear in the database")
        # Displays the following information if user selects option 2
    elif ans=="2":
        department=input("\n Enter the department name:")
        if department in departmentName:
            deptIndex=departmentName.index(department)
            location=departmentLocation[deptIndex]
            budget=departmentBudget[deptIndex]
            print("\nDepartment Location: "+location)
            print("Department Budget: $"+str(budget))
            print("Instructors that work for the department: ")
            for i in range (len(instructorName)):
                if instructorDept[i]==department:
                    print(instructorName[i])
        else:
            print("\nThe department name does not appear in the database")
        #Displays the following information if user selects option 3
    elif ans=="3":
        id=input("\n Enter the instructor id:")
        name=input("\n Enter the instructor name:")
        department=input("\n Enter the affiliated department name:")
        print ("\n Instructor id: " + id)
        print ("\n Instructor name: " + name)
        print ("\n Affiliated department name: " + department)
        if(department not in departmentName):
            print("\nThe department does not exist and hence the instructor record cannot be added to the database\n")
        if (id in instructorID):
            print("\nInstructor id already exists\n")
        instructorID.append(id)
        instructorName.append(name)
        instructorDept.append(department)
        
# Print goodbye if user selects option 4
    elif ans=="4":
        print("\n Goodbye")
        break
      
    else:
        print("\n Not Valid Choice Try again")
