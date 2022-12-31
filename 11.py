def main():
    start = int(input("Enter the start range "))
    end = int(input("Enter the end range "))
    if (start == 1 or 0) or (end == 1 or 0):
        print("1 or 0 is neither prime nor composite...")
    else:
        for i in range(start, end+1):
            for j in range(2, i):
                if i%j == 0:
                    break
            else:
                print(i, end=" ")
            



if __name__ == "__main__":
    print("Program to print prime numbes within a range")
    main()