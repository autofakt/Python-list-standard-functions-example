'''
Programmer: 
Description: Create a menu to allow the user to add, insert, remove, find the maximum, the minimum, and 
sort the list in descending order (larger to smaller value). Declare your list as list of string.
Date: 06/27/2019
'''
studentFullName = []
option = 0 #default setting

while(option != 7):
    print("=====================================")
    print("               |Menu|")
    print("1 - Add an item to the list")
    print("2 - Remove an item from the list")
    print("3 - Insert an item to the list")
    print("4 - Find maximum")
    print("5 - Find minimum")
    print("6 - Sort the list in descending order")
    print("7 - Quit the program")
    print("8 - Reverse list")
    print("9 - Print list")
    option = int(input("Please select an option: "))
    print("=====================================")
    print()
    
    if (option == 1):
        print("Before operation: ",studentFullName)
        item = input("Please add name to the list: ")
        studentFullName.append(item)
        print("After operation: ",studentFullName)
        print()
    
    if (option == 2):
        if(len(studentFullName)==0): # display error message if list is empty
            print("List is empty, cannot remove an item")
        #while(len(studentFullName)>0): # does not allow you to enter loop while list empty     
        if(len(studentFullName)>0):
            print("List len: ",len(studentFullName))
            option2 = input("Remove by name or index? (N for name I for index): ").upper()
            
            if option2 != 'N' and option2 != "I":
                print("Must be N or I, try again.")
                option2 = input("Remove by name or index? (N for name I for index): ").upper()
            if option2 == 'N':
                print("Before operation: ",studentFullName)
                itemName = input("Item # remove from the list: ")
                while(itemName not in studentFullName):  # Error checking
                    print("Not in list, try again")
                    itemName = input("Item # remove from the list: ")
                studentFullName.remove(itemName)
                print("After operation: ",studentFullName)
                print()
                continue
            if option2 == "I":
                print("Length of list: ", len(studentFullName))
                print("Before operation: ",studentFullName)
                itemNum = int(input("Index of item to remove from the list: "))
                while itemNum > len(studentFullName)-1 or itemNum <0:  # error checking index #
                    print("Index out of bounds, try again")
                    itemNum = int(input("Index of item to remove from the list: "))
                studentFullName.remove(studentFullName[itemNum])
                #del studentFullName[itemNum:itemNum+1]  # can use this without error checking
                print("After operation: ",studentFullName)
                print()
    
    if option == 3:
        print("List len: ",len(studentFullName))
        print("Before operation: ",studentFullName)
        index = int(input("Index # of where to insert (starts at 0): "))
        if len(studentFullName)==0:   # error checking for empty list
            index = 0
            item = input("Insert name to the list: ")
            studentFullName.insert(index,item)
            print("After operation: ",studentFullName)
            print()
            continue
        while index > len(studentFullName)-1 or index <0:  # error checking index #
                print("Index out of bounds, try again")
                index = int(input("Index # of where to insert: "))
        item = input("Insert name to the list: ")
        studentFullName.insert(index,item)
        print("After operation: ",studentFullName)
        print()
        
    if option ==4:
        if len(studentFullName)==0:  # error checking for empty list
            print("List is empty, cannot get value")
        else:
            maxValue = studentFullName[0]
            print("Before operation: ",studentFullName)
            #manual version without built in max function
            ''''
            for i in studentFullName:  
                if (i>maxValue):
                   maxValue = i
            '''
            maxValue = max(studentFullName)
            print("Max Value: ", maxValue)
            print("After operation: ",studentFullName)
        
    if option == 5:
        if len(studentFullName)==0:  # error checking for empty list
            print("List is empty, cannot get value")
        else:
            minValue = studentFullName[0]  # sets the first index value as min because a blank will always be lowest
            print("Before operation: ",studentFullName)
            #manual version without built in min function
            '''
            for i in studentFullName:
                if (i<minValue):
                    maxValue = i
            '''
            minValue = min(studentFullName)
            print("Min Value: ", minValue)
            print("After operation: ",studentFullName)
    
    if option ==6:
        print("Before operation: ",studentFullName)
        studentFullName.sort(reverse=True)  # sorts in descending order
        print("After operation: ",studentFullName)
        
    if option ==8:
        print("Before operation: ",studentFullName)
        studentFullName.reverse()  # reverses the list
        print("After operation: ",studentFullName)
        
    if option ==9:
        print("Current Print: ",studentFullName)
        
