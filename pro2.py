# Import Section

from datetime import date  # To import date
import getpass            # To import username

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
fname = []
lname = []
doby = []
for i in range(0,n+1):
    first  = input("Enter the first name ")
    last = input("Enter the last name ")
    dob = input("Enter the birth year ")
    
    fname.append(first)
    lname.append(last)
    doby.append(dob)

# Process Section

zipper = zip(fname, lname, doby)
username = []
employee = {}
for i in range(0, n+1):
    uname = fname[i][1].lower() + lname[i] + doby[i][-2:]
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
print("All zip data ", zipper)
print("Username list with all usernames(even the duplicates) ", username)
print("Username set ", dupli)
print("Username list with no duplicates ", frlist)
print("Employee data dictionary ", employee)
print("Username list that has been sorted ", sorted(frlist))

