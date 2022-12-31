# Import Section

from datetime import date  # To import date
import getpass             # To import username

# Flower Box Section

####################################################
#
# Name : Joffin George
# Date : 20/10/2022
# Program Description :
# 
# This includes working with strings, numbers and comments.
# You will also need to use the input function  
#
####################################################

# Input Section

temp = float(input("Enter the Farhenheit to calculate in Celcius "))
name = input("Enter the name ")

# Process Section

upper = name.upper()
lower = name.lower()
title = name.title()
namel = len(name)

index1 = name[0]
index2 = name[-1]
index3 = name[1:]

fstring = f'Hello {title}, your name is {namel} long!'
cstring = "Hello " + title + " your name is " + str(namel) + " long! "
mulstring  = name * 10

celfloat = (temp-32)*5/9
celint = int(celfloat)


# Output Section

print("Username ", getpass.getuser())
print("Today's Date ", date.today())
print("Name entered by user ", name)
print("Type of variable that name is ", type(name))
print("The 3 case variables upper, lower and title (proper case) ", upper, lower, title)
print("First Initial of name ", index1)
print("The last character of name ", index2)
print("Name from 2 position to end of string ", index3)
print("The fstring message ",fstring)
print("The concatenated message ",cstring)
print("Celcius float variable followed by its type ", celfloat, type(celfloat))
print("Celcius int variable followed by its type ", celint, type(celint))
