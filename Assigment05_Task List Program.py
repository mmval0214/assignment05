# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,2.1.2023,Created started script
# MMVa,2.18.2023,Added code to complete assignment 5
# ----------------------------------------------------------------------- #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A variable to capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

try:
    objFile = open("ToDoList.txt", "r")  # open  file
    print("|============================================|")
    print("|These are the current tasks you have saved: |")
    print("|============================================|")
    for row in objFile:  # find rows
        lstRow = row.split(',')  # split items
        dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}  # create dic with items
        print('\t' + dicRow["Task"] + ' | ' + dicRow["Priority"].strip())  # print
    objFile.close()  # close
except:  # error handling
    print("File not found")  # if file not found

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current entered tasks
    2) Add a new tasks
    3) Remove an existing tasks
    4) Save task to File
    5) Exit Program
    """)  # Menu options

    strChoice = str(input("Select an option to perform? [1 to 5]: "))  # User selection
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    #   TODO: Add Code Here
    if strChoice.strip() == '1':
        objFile = open("ToDoList.txt", "r")  # open  file
        print("Current tasks saved to file:")
        for row in objFile:
            lstRow = row.split(',')
            dicRow = {"Item": lstRow[0].strip(), "Priority": lstRow[1].strip()}
            print('\t' + dicRow["Item"] + ' | ' + dicRow["Priority"])
        objFile.close()
        continue

    # Step 4 - Add a new item to the list/Table
    # TODO: Add Code Here
    elif strChoice.strip() == '2':  # validates user selection
        dicName = input("Enter a new task name: ")  # user input
        dicRank = input("Enter its priority ['Low', 'Medium', 'High'):")  # user input
        dicRow = {"Item": dicName.strip(), "Priority": dicRank.strip()}  # create dictionary
        lstTable.append(dicRow) # add dictionary rows to table
        print("|============================================|")
        print("| So far you have the following new tasks:   |")
        print("|============================================|")
        print("Task", "|", "Priority")  # headings
        for row in lstTable:  # all rows are printed
            print(row["Item"] + ' | ' + row["Priority"]) # print values for each key
        continue  # move on


    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):   # validates user selection
        # TODO: Add Code Here
        TskDlt = input("Which task would you like to remove? ")  # input
        bIntItemRemoved = False  # boolean flag
        RowNumb = 0 #counter
        while (RowNumb < len(lstTable)):  # loop
            if (TskDlt == str(list(dict(lstTable[RowNumb]).values())[0])):  # comparison
                del lstTable[RowNumb]  # delete
                bIntItemRemoved = True  # if deleted then True
            RowNumb += 1 # adds as go through table
        if (bIntItemRemoved == True):  # if item found confirms
            print("You task has been removed:", TskDlt)
        else: # if item not found
            print("Value", TskDlt, "could not be found")  # not found
        print("Your remaining tasks are:")  # prints remaining items
        for row in lstTable:
            print(row["Item"] + ' | ' + row["Priority"])
            continue  # move on

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        print("|=======================|")
        print("| Your saved tasks are: |")
        print("|=======================|")
        for row in lstTable:  # Finds rows in table
            print(row["Item"] + ' | ' + row["Priority"])  # Print
        objFile = open("ToDoList.txt", "w")  # Open file
        for row in lstTable:  # Rows in the table
            objFile.write(row["Item"] + ', ' + row["Priority"] + "\n")  # Save to file
        objFile.close()  # Close
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):  # Validate user selection
        # TODO: Add Code Here
        print("You have ended the program...goodbye!")  # Print
        break  # Exit the program
