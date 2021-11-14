#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Tcaetano, 20211111, changed file to assignment V
# Tcaetano, 20211112, substituted lists for dictionaries
# Tcaetano, 20211113, added  more functionality to some of the loops
#------------------------------------------#

# Declare variables

strChoice = '' # User input
list_table = []  # list of lists to hold data
# TODO replace list of lists with list of dicts
list_row = []  # list of data row
filename = 'CDInventory-A.txt'  # data storage file
object_file = None  # file object
dict_row = {}
string_row = ''

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        break
    
    if strChoice == 'l':
        # TODO Add the functionality of loading existing data
        list_table.clear()
        object_file = open(filename, 'r')
        for row in object_file:
        #------------------------------------------------------------------
        # just highlighting an area I have difficulty undertanding
                string_row = row.strip().split(',')
                dict_row = { 'ID': string_row[0], 'Title': string_row[1], 'Artist': string_row[2]}
                list_table.append(dict_row)
        # -----------------------------------------------------------------
        object_file.close()        
    
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        ID = int(input('Enter an ID: '))
        title = input('Enter the CD\'s Title: ')
        artist = input('Enter the Artist\'s Name: ')
        dict_row = {'ID': ID, 'Title': title, 'Artist': artist}
        list_table.append(dict_row)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID,    CD Title,    Artist')
        for row in list_table:
            print(*row.values(), sep=',\t\t') 
    
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
         print('ID,    CD Title,    Artist')
         for row in list_table:
            print(*row.values(), sep=',\t\t')  
         
         ID_deletion = int(input('Which ID do you wish to delete? '))
         for row in list_table:
             print(row)
             if row['ID'] == ID_deletion:
                 list_table.remove(row)
         
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        object_file = open(filename, 'w')
        for row in list_table:
            for content in row.values():
                string_row = string_row + str(content) + ','
            string_row = string_row[:-1] + '\n'
        object_file.write(string_row)
        object_file.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

