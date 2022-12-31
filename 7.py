#!/usr/bin/python3

num1=int(input("Enter the number 1"))
num2=int(input("Enter the number 2"))
num3=int(input("Enter the number 3"))

if(num1>num2):
    if(num1>num3):
        print("Greatest number", num1)
    else:
        print("Greatest number", num3)
if(num2>num1):
    if(num2>num3):
        print("Greatest number", num2)
    else:
        print("Greatest number", num3)

