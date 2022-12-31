#!/usr/bin/python3

num = int(input("Enter the number"))
flag = 1
for i in range(2, int(num/2)):
    if(num%i==0):
        flag=0
        break
if(flag==1):
    print("Prime")
else:
    print("Not prime")
        
