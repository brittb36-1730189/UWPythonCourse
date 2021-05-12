# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BBritt,5.8.2021,Added code to complete assignment 5
# BBritt,5.9.2021,Edited code I added
# BBritt,5.10.2021,Added comments
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = "" # A Capture the user option selection
lstRow = []
newTask = ""
newPriority = ""


# -- Processing -- #
# Step 1 - When the program starts, load the data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open('ToDoList.txt', 'r') #open text file
for row in objFile:
    lstRow = row.split(',') #separate data by ','
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()} #create dictionary by defining keys
    lstTable.append(dicRow) #need to append when opening existing file or no existing data prints later
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow) #print contents of table
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = str(input('Enter new task: ')) #define the new task and get user input
        newPriority = str(input('Enter new priority: ')) #define the new priority and get user input
        dicRow = {'Task': newTask, 'Priority': newPriority} #add new task and priority to dictionary
        lstTable.append(dicRow) #add new data to the existing table
        print('The task of',newTask, 'and priority of', newPriority, 'has been entered')
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        for dicRow in lstTable:
            rowNumber = lstTable.index(dicRow) #get the row number of each dictionary within the lstTable
            print(rowNumber, '--->', dicRow.items()) #print the row numbers and each dictionary for user reference
        removeRow = int(input("Choose the row you would like to remove. Enter row number: ")) #user identifies row to remove
        del lstTable[removeRow] #deletes the row that user identified
        print('Row', removeRow, 'has been removed')
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w') #open the file in the "write" format so new text can be added
        print('Your data has been saved')
        for dicRow in lstTable:
            objFile.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n') #save data in
        objFile.close()
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        break  # and Exit the program
