def main():
    n = int(input("Enter the number of times you want to enter the number"))
    for i in range(0, n+1):
        num = int(input("Enter the number"))
        if num%5 == 0:
            print("Hello")
        else:
            print("Bye")
if __name__ == "__main__":
    print("Program to print Hello or Bye based on multiple of 5...")
    main()