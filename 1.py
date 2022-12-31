#!/usr/bin/python3

def hcf(num1, num2):
    max = 0
    for i in range(1, min(num1, num2)):
        if num1%i == 0 and num2%i == 0:
            max = i
    print("The HCF is :", max)

def main():
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    hcf(num1, num2)

if __name__ == '__main__':
    main()
