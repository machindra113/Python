#!/usr/bin/python3

def lcm(num1, num2):
    pass
    lcm = 0
    for i in range(1, max(num1, num2)):
        if i%num1 == 0 or i%num2 == 0:
            lcm = i
    print("The lcm is :", lcm)

def main():
    num1 = int(input("Enter the first number :"))
    num2 = int(input("Enter the second number :"))
    lcm(num1, num2)
    pass

if __name__ == '__main__':
    main()
