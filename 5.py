#!/usr/bin/python3

start=int(input("Enter the start limit :"))
end=int(input("Enter the end limit :"))
sum = 0
for i in range(start,end+1):
    sum=sum+i
print("Sum is", sum)
