#List of instructors ID
instructorID = ["1", "2", "3", "4"]

#List of instructors names
instructorName = ["Tian Tian", "Marvin Bishop", "Kashifuddin Qazi", "Sr.Joan"]

#List of instructors departments
instructorDept = ["CS", "Math", "CS", "Math"]

while True:
    department = input("\nEnter department name(Press -1 when your finished): ")
    if department in instructorDept:
        deptIndex=instructorDept.index(department)
        name=instructorName[deptIndex]
        id=instructorID[deptIndex]
        idIndex=instructorID.index(id)
        for i in range (len(instructorName)):
                    if instructorDept[i]==department:
                        print(instructorName[i])
    elif department == "-1":
        break
    else:
        print("\nNo instructors found")

