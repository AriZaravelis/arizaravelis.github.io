#Aldona Neziraj
#Dorian Ryan
#Ari Zaravelis

#Report: We all contributed to this project by meeting up after class and working on it together.


tinyc = open(" ", "r") #Opens file and reads it. Add file path between the double quotes.
output = open(" ", "w") #Opens file and writes to it. Add file path between the double quotes.
output.truncate(0) #Removes the contents of the token file for each run

with tinyc as f:
    tinyCfile = f.read().splitlines() #Splits the file lines into a list

#Symbols and Operators
LP = "("
RP = ")"
ASGN = "="
SC = ";"
ADD = "+"
SUB = "-"
COMPARE = "<" or ">"

#Keywords
IF = "if"
THEN = "then"
ELSE = "else"
WHILE = "while"
DO = "do"


tinyCList = [] #New list

length =(len(tinyCfile)) #Length of the list


for i in range(0, length, +1): #Outer for loop that iterates in a specific range
    for x in range(len(tinyCfile[i])): #Inner for loop that iterates over characters position at a specific index
        tinyCList.append(tinyCfile[i][x])

m = 0 #Counter
while m < len(tinyCList):
    if tinyCList[m] >= 'a' and tinyCList[m] <= 'z': #Checks if it's a valid character

        #Checks if keyword is WHILE
        if tinyCList[m] == 'w' and tinyCList[m+1] == 'h' and tinyCList[m+2] == 'i':
            output.write("WHILE: "+"\""+WHILE+"\"\n")
            m += 5
            continue
        #Checks if keyword is DO
        elif tinyCList[m] == 'd' and tinyCList[m+1] == 'o':
            output.write("DO: "+"\""+DO+"\"\n")
            m += 2
            continue
        #Checks if keyword is ELSE
        elif tinyCList[m] == 'e' and tinyCList[m+1] == 'l' and tinyCList[m+2] == 's':
            output.write("ELSE: "+"\""+ELSE+"\"\n")
            m += 4
            continue
        #Checks if keyword is IF
        elif tinyCList[m] == 'i' and tinyCList[m+1] == 'f':
            output.write("IF: "+"\""+IF+"\"\n")
            m += 2
            continue
        #Checks if keyword is THEN
        elif tinyCList[m] == 't' and tinyCList[m+1] == 'h' and tinyCList[m+2] == 'e' and tinyCList[m+3] == 'n':
            output.write("THEN: "+"\""+THEN+"\"\n")
            m += 4
            continue
        #Checks for identifier
        else:
            output.write("id: "+"\""+tinyCList[m]+"\"\n")
            m += 1
            continue
        #Checks for numbers
    elif tinyCList[m] >= "0" and tinyCList[m] <= '9':
        output.write("num: "+"\""+tinyCList[m])
        m += 1
        while tinyCList[m] >= "0" and tinyCList[m] <= '9':
            output.write(tinyCList[m])
            m += 1
        output.write("\"\n")
        continue
    elif tinyCList[m] == LP: #Checks if the symbol is LP
        output.write("LP: "+ "\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == RP: #Checks if the symbol is RP
        output.write("RP: "+"\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == ASGN: #Checks if the symbol is ASGN
        output.write("ASGN: "+"\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == SC: #Checks if the symbol is SC
        output.write("SC: "+"\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == ADD: #Checks if the operator is ADD
        output.write("ADD: ""\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == SUB: #Checks if the operator is SUB
        output.write("SUB: ""\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == COMPARE: #Checks if the operator is COMPARE
        output.write("COMPARE: "+"\""+tinyCList[m]+"\"\n")
        m += 1
        continue
    elif tinyCList[m] == ' ': #Ignores whitespace
        m += 1
        continue
    else:
        output.write("LEXICAL_ERROR") #Lexical error if none of the above if statements are correct
    break


#Closes both files
tinyc.close()
output.close()

