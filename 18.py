def main():
    year = int(input("Enter the year "))
    if year%400 == 0 and year%100 == 0:
        print("This is a leap year")
    elif year%4 == 0 and year%100 != 0:
        print("This is a leap year")
    else:
        print("This is not a leap year")
        
if __name__ == "__main__":
    print("Program to print whether the year eneterd is leap year or not")
    main()