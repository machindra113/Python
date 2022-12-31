# Import Section

from datetime import date  # To import date
import getpass             # To import username

# Flower Box Section

####################################################
#
# Name : Joffin George
# Date : 25/10/2022
# Program Description :
# 
# This includes working with lists, tuples, dictionaries and sets.
# You will also need to use the input function
# This program will use 3 different list (that you will create) that contain information about employees.
# This program will take input from 3 different list that you create.
# The first list will contain 5 first names, the second list will contain 5 last names, and the third list will contain 5 birth years.
# These lists will be combined and then used to create a unique username. 
# You will remove any duplicate usernames (you must have at least one in the original list). 
# You will also create a dictionary to store the username in as a key with the combined employee data created in the combination process.  
#
####################################################

# Input Section

n = int(input("Enter the number of entries to be made(Min 5) "))
while n > 5:
    fname = []
    lname = []
    doby = []
    ch =""

    def add():
        for i in range(0,n+1):
            first  = input("What's your first name ")
            last = input("What's your last name ")
            dob = input("What year were you born ")
            if len(first) > 2 and len(lname) > 2 and len(dob) == 4:
                fname.append(first)
                lname.append(last)
                doby.append(dob)
            else:
                print("Name should be atleast 2 characters and dob should be atleast 4 characters ")
    add()

    print("The first name list :", fname)
    print("The last name list :", lname)
    print("The date of birth list :", doby)
    print("Are you sure the information entered is correct?(Y/N)", ch)
    if ch == 'y' or 'Y':
        print("Proceeding further...")
    elif ch == 'n' or 'N':
        print("Enter the correct data again...")
        fname.clear()
        lname.clear()
        doby.clear()
        add()
    else:
        print("Enter correct choice...")

    # Process Section

    zipper = zip(fname, lname, doby)
    username = []
    employee = {}
    for i in range(0, n+1):
        uname = fname[i][1].lower() + lname[i] + doby[i][-2:]
        if uname in username:
            uname = fname[i].lower() + lname[i][1] + doby[i][-2:]
            username.append(uname)
        else:
            username.append(uname)
        employee.update({username[i]:(fname[i],lname[i],doby[i])})

    dupli = set(username)
    frlist = list(dupli)

    for i in username:
        newlist = []
        if i in newlist:
            break
        else:
            newlist.append(i)

    # Output Section

    print("Username ", getpass.getuser())
    print("Today's Date ", date.today())
    print("All zip data ", print(zipper))
    print("Username list with all usernames(even the duplicates) ", username)
    print("Username set ", dupli)
    print("Username list with no duplicates ", frlist)
    print("Employee data dictionary ", employee)
    print("Username list that has been sorted ", sorted(newlist))

else:
    print("Enter 5 or more ")