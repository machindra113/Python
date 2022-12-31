def main():
    num = int(input("Enter the number to end "))
    ls = []
    for i in range(0, num+1):
        if i == 0:
            ls.append(0)
        elif i == 1:
            ls.append(1)
        else:
            ls.append(ls[i-1]+ls[i-2])
    print(ls)
if __name__ == "__main__":
    print("Program to print Fibonacci series...")
    main()