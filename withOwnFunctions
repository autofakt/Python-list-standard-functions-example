'''
Programmer:
Description: Create a menu to allow the user to add, insert, remove, find the maximum, the minimum, and 
sort the list in descending order (larger to smaller value). Declare your list as list of string.  Use your own functions
instead of the built-in ones.
Date: 07/05/2019
'''


    
studentFullName = []
option = 0 #default setting

def myLength(item):
    total = 0
    for x in item:
        total += 1
    return total

def addItem(item):
    temp = [item]
    studentFullName[myLength(studentFullName):] = temp
    
def removeItem(item):
    target = studentFullName.index(item)
    new_list = studentFullName[0:target] + studentFullName[target+1:]
    return new_list
    
def removeItemByIndex(index):
    target = index
    new_list = studentFullName[0:target] + studentFullName[target+1:]
    return new_list

def insertToList(item, index):
    temp = [item]
    left = studentFullName[0:index]
    right = studentFullName[index:]
    new_list = left + temp + right
    return new_list
    
def findMax(myList):
    maxValue = studentFullName[0]
    for i in myList:  
        if (i>maxValue):
            maxValue = i
    return maxValue

def findMin(myList):
    minValue = studentFullName[0]
    for i in myList:  
        if (i<minValue):
            minValue = i
    return minValue

def sortList(mylist):
    question = input("In (A)scending or (D)esending order?: ").upper()
    while question != 'A' and question != 'D':
        print('Select only A or D, try again.')
        question = input("In (A)scending or (D)esending order?: ").upper()
    for x in range(len(mylist)):
        for x in range(myLength(mylist)-1):
            if question == 'D':
                if mylist[x] < mylist[x+1]:
                    temp = mylist[x]
                    mylist[x] = mylist[x+1]
                    mylist[x+1] = temp
            else:
                if mylist[x] > mylist[x+1]:    
                    temp = mylist[x]
                    mylist[x] = mylist[x+1]
                    mylist[x+1] = temp
    return mylist

def displayList(myList):
    print(myList)
    
def reverseList(myList): 
    return myList[::-1]     # reverse list using slicing

                  
while(option != 9):     # Full menu of operations
    print("=====================================")
    print("               |Menu|")
    print("1 - Add an item to the list")
    print("2 - Remove an item from the list")
    print("3 - Insert an item to the list")
    print("4 - Find maximum")
    print("5 - Find minimum")
    print("6 - Sort list")
    print("7 - Reverse list")
    print("8 - Display list")
    print("9 - Quit the program")
    option = int(input("Please select an option: "))
    print("=====================================")
    if option == 9:  # exit message
        print("       Thank you, bye!")
    print()
    
    if (option == 1):  # Add item
        print("Before operation: ", end='')
        displayList(studentFullName)
        item = input("Please add name to the list: ")
        addItem(item)
        print("After operation: ", end='')
        displayList(studentFullName)
        print()
    
    if (option == 2):  # Remove item by name or index number
        if(myLength(studentFullName)==0): # display error message if list is empty
            print("List is empty, cannot remove an item")
        if(myLength(studentFullName)>0):  # if list is not empty
            option2 = input("Remove by name or index? (N for name I for index): ").upper()
            if option2 != 'N' and option2 != "I":  # input must be N or I
                print("Must be N or I, try again.")
                option2 = input("Remove by name or index? (N for name I for index): ").upper()
            if option2 == 'N':
                print("Before operation: ", end='')
                displayList(studentFullName)
                itemName = input("Item name to remove from the list: ")
                while(itemName not in studentFullName):  # Error checking if item not in list
                    print("Not in list, try again")
                    itemName = input("Item name to remove from the list: ")
                studentFullName = removeItem(itemName)
                print("After operation: ",studentFullName)
                print()
                continue
            if option2 == "I":
                print("Before operation: ", end='')
                displayList(studentFullName)
                itemNum = int(input("Index of item to remove from the list: "))
                while itemNum > myLength(studentFullName)-1 or itemNum <0:  # error checking index #
                    print("Index out of bounds, try again")
                    itemNum = int(input("Index of item to remove from the list: "))
                studentFullName = removeItemByIndex(itemNum)
                #del studentFullName[itemNum:itemNum+1]  # can use this without error checking
                print("After operation: ",studentFullName)
                print()
    
    if option == 3:  # insert item at the ends or anywhere in between. 
        print("Before operation: ", end='')
        displayList(studentFullName)
        index = int(input("Index # of where to insert (starts at 0): "))
        if len(studentFullName)==0:   # error checking for empty list
            index = 0
            item = input("Insert name to the list: ")
            studentFullName = insertToList(item, index)
            print("After operation: ", end='')
            displayList(studentFullName)
            print()
            continue
        while index > len(studentFullName)-1 or index <0:  # error checking index #
                print("Index out of bounds, try again")
                index = int(input("Index # of where to insert: "))
        item = input("Insert name to the list: ")
        studentFullName = insertToList(item,index)
        print("After operation: ", end='')
        displayList(studentFullName)
        print()
        
    if option ==4:  # finding the maximum in list
        if len(studentFullName)==0:  # error checking for empty list
            print("List is empty, cannot get value")
        else:
            print("Before operation: ", end='')
            displayList(studentFullName)
            maxValue = findMax(studentFullName)
            print("Max Value: ", maxValue)
            print("After operation: ", end='')
            displayList(studentFullName)
        
    if option == 5:  # finding the minimum in list
        if len(studentFullName)==0:  # error checking for empty list
            print("List is empty, cannot get value")
        else:
            print("Before operation: ", end='')
            displayList(studentFullName)
            minValue = findMin(studentFullName)
            print("Min Value: ", minValue)
            print("After operation: ", end='')
            displayList(studentFullName)
    
    if option ==6:   # sort the list in either ascending or desending order
        print("Before operation: ", end='')
        displayList(studentFullName)
        studentFullName = sortList(studentFullName)
        print("After operation: ", end='')
        displayList(studentFullName)
        
    if option ==7:  # reverse the list
        print("Before operation: ", end='')
        displayList(studentFullName)
        studentFullName = reverseList(studentFullName)
        print("After operation: ", end='')
        displayList(studentFullName)
        
    if option ==8:  #display list
        print("Current List: ", end='')
        displayList(studentFullName)
