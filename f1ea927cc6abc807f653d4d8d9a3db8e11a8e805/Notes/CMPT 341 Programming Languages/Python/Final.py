import mysql.connector

connect = mysql.connector.connect(user= 'root', password='7698frza')
c = connect.cursor()    

c.execute(("""create database bank;"""))
c.execute("""use bank""")

c.execute("""create table customer(customerID int(50) PRIMARY KEY, firstName varchar(50), middleName varchar(50), lastName varchar(50), dateOfBirth date, address varchar(50), phoneNum varchar(15), email varchar(50));""")

c.execute("""create table bankingAccount(accountNum int(50) PRIMARY KEY, customerID int (50), FOREIGN KEY(customerID) references customer(customerID), username varchar(50), password varchar(50), currentBalance int(30), availableBalance int(30));""")

c.execute("""create table accountHistory(accountNum int(50) PRIMARY KEY, FOREIGN KEY(accountNum) references bankingAccount(accountNum), dateAccountCreated date, numWithdrawals int(50), numDeposits int(50));""")

c.execute("""create table recentTransaction(accountNum int(50) PRIMARY KEY, FOREIGN KEY(accountNum) references bankingAccount(accountNum), dateOfWithdrawal date, dateOfDeposit date, amountWithdrawn int(30), amountDeposited int(30));""")



customer = [("1", "Ari", "Spiro", "Zaravelis", "1999-11-13", "910-Split Rock Road-Pelham-NY", "9142813693", "zaravelisa@gmail.com"),
             ("2", "Autumn", "Lily", "Tremblay", "1967-02-20", "8552-Gonzales Street-New Brunswick-NJ", "3707662105", "tremblay1827@gmail.com"),
             ("3", "Theodore", "Grey", "Smith", "1987-09-07", "51-Chapel Avenue-Aliquippa-PA", "7242704109", "smith0101@gmail.com"),
             ("4", "Madeline", "Harper", "Johnson", "1993-12-15", "934-Heather Lane-Clarksville-TN", "4562419292", "johnson246@gmail.com"),
             ("5", "Braden", "Daniel", "Miller", "1991-02-06", "701-Thompson Road-Bristol-CT", "5786539704", "miller987@gmail.com"),
             ("6", "Sophia", "Maud", "Williams", "1989-09-15", "928-Fawn Street-Gettysburg-PA", "5284858283", "williams7676@gmail.com"),
             ("7", "Maverick", "Ross", "Wilson", "1971-10-18", "97-North Alton Street-Knoxville-TN", "6221421231", "wilson2121@gmail.com"),
             ("8", "Shane", "Richard", "Jackson", "1988-07-02", "30-Lower River Street-Vernon Hills-IL", "6347619021", "jacksons123@gmail.com"),
             ("9", "Oliver", "Hudson", "Lee", "1995-11-19", "9056-South Valley Avenue-Anderson-SC", "7612317685", "lee213@gmail.com"),
             ("10", "Dustin", "Blake", "Harris", "1990-03-18", "3-Woodsman Street-Streamwood-IL", "5614227871", "Harris135@gmail.com")]

bankingAccount = [("2000", "1", "Morgan123456", "123pizza", "7000", "6000"),
                   ("2001", "2", "Parataxis", "y27hgo", "25000", "25000"),
                   ("2002", "3", "Besomfen826", "e8r6ta", "12329", "12329"),
                   ("2003", "4", "Toponym", "lra6uu", "54000", "54000"),
                   ("2004", "5", "Zulede714", "lideb77g", "2100", "1600"),
                   ("2005", "6", "Barracoon", "0964ljax", "12200", "12200"),
                   ("2006", "7", "Elephantom", "yiil679", "434", "434"),
                   ("2007", "8", "Quinzee", "uk2rmwn", "67000", "67000"),
                   ("2008", "9", "Higgler", "5img2p6", "21000", "21000"),
                   ("2009", "10", "Yonderly", "rwg46sf", "9753", "9121"),]

accountHistory = [("2000", "2018-10-18", "3", "12"),
                    ("2001", "2016-03-11", "9", "21"),
                    ("2002", "2017-05-09", "6", "17"),
                    ("2003", "2014-09-15", "12", "31"),
                    ("2004", "2018-11-20", "2", "7"),
                    ("2005", "2017-07-17", "5", "15"),
                    ("2006", "2019-04-07", "1", "3"),
                    ("2007", "2013-09-03", "12", "42"),
                    ("2008", "2016-08-12", "13", "19"),
                    ("2009", "2017-01-11", "6", "14"),]

recentTransaction = [("2000", "2019-11-18", "2019-10-15", "545", "1200"),
                      ("2001", "2019-12-10", "2019-11-25", "1200", "2100"),
                      ("2002", "2019-11-18", "2019-10-19", "1320", "700"),
                      ("2003", "2019-11-09", "2019-11-02", "1280", "2100"),
                      ("2004", "2019-12-02", "2019-12-10", "423", "1080"),
                      ("2005", "2019-11-22", "2019-09-12", "1280", "783"),
                      ("2006", "2019-11-21", "2019-11-05", "66", "500"),
                      ("2007", "2019-10-18", "2019-10-02", "1240", "985"),
                      ("2008", "2019-09-03", "2019-12-23", "732", "982"),
                      ("2009", "2018-04-24", "2019-10-15", "210", "892"),]

c.executemany("insert into customer(customerID, firstName, middleName, lastName, dateOfBirth, address, phoneNum, email) values (%s, %s ,%s, %s, %s, %s, %s, %s)", customer)
c.executemany("insert into bankingAccount(accountNum, customerID, username, password, currentBalance, availableBalance) values (%s, %s ,%s, %s, %s, %s)", bankingAccount)
c.executemany("insert into accountHistory(accountNum, dateAccountCreated, numWithdrawals, numDeposits) values (%s, %s, %s, %s)", accountHistory)
c.executemany("insert into recentTransaction(accountNum, dateOfWithdrawal, dateOfDeposit, amountWithdrawn, amountDeposited) values (%s, %s, %s, %s, %s)", recentTransaction)



print("""
    1.Insert a record about a new customer.
    2.Delete a record about account history and most recent transaction.
    3.Display the total count of people in the database.
    4.Enter customer ID and I will provide the name and username associated with it.
    5.Exit
    """)


while True:
    ans=input("What would you like to do?")


    
#Insert a record about a new customer.
    if ans=="1":
        idInput = input("Enter the customer id: ")
        accountNumInput = input("Enter the customer account number: ")
        firstNameInput = input("Enter the customer's first name: ")
        middleNameInput = input("Enter the customer's middle name: ")
        lastNameInput = input("Enter the customer's last name: ")
        dateOfBirthInput = input("Enter the customer's date of birth(Ex:1991/03/14): ")
        addressInput = input("Enter the customer's address: ")
        phoneNumInput = input("Enter the customer's phone number: ")
        emailInput = input("Enter the customer's email: ")
        usernameInput = input("Enter the customer's username: ")
        passwordInput = input("Enter the customer's password: ")
        currentBalanceInput = input("Enter the current balance: ")
        availableBalanceInput = input("Enter the available balance: ")

        if(idInput in 'customer'):
            print("Customer id already exists")
        else:
            c.execute("insert into customer(customerID, firstName, middleName, lastName, dateOfBirth, address, phoneNum, email) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                      (idInput, firstNameInput, middleNameInput, lastNameInput, dateOfBirthInput, addressInput, phoneNumInput, emailInput))
            c.execute("insert into bankingAccount(accountNum, customerID, username, password, currentBalance, availableBalance) values(%s,%s,%s,%s,%s,%s)",
                      (accountNumInput, idInput, usernameInput, passwordInput, currentBalanceInput, availableBalanceInput))
            print("\nValues have been recorded.\n")
            connect.commit()



#Deletes a record about account history and most recent transaction.
    elif ans=="2":
        accountNumInput=input("\nEnter the account number and I will delete the account history and well as the most recent transaction:")
        c.execute("delete from recentTransaction where accountNum =  '{}'".format(accountNumInput))
        c.execute("delete from accountHistory where accountNum =  '{}'".format(accountNumInput))
        connect.commit()
        print("records deleted")



#Displays total count of people in the database
    elif ans == "3":
        c.execute("select count(customerID) from customer")
        result = c.fetchall()
        if len(result) == 0:
            print("No usernames found.")
        else:
            for i in result:
                user = (i[0])
                print (user)
        
        

#Provides the name and username associated with customer ID.
    elif ans == '4':
      idInput = input("Enter the customer id: ")

      print("Customer Name: ")
      c.execute("""select firstName, middleName, lastName from customer where customerID = '{}'""".format(idInput))
      result = c.fetchall()
      if len(result) == 0:
          print("No customers found.")
      else:
          for i in result:
              print(i[0])
              
      print("Affiliated username: ")
      c.execute("""select username from bankingAccount where customerID = '{}'""".format(idInput))
      result = c.fetchall()
      if len(result) == 0:
          print("No usernames found.")
      else:
          for i in result:
              user = (i[0])
              print (user)

        


#Stops while loop and finishes the program     
    elif ans=="5":
        print("\nGoodbye")
        exit()
        break


connect.close()
