def main():
    for i in range(100, 1000+1):
        if i%5 == 0 and i%7 == 0:
            print(i, end=" ")
if __name__ == "__main__":
    print("Program to print range from 100 to 1000...")
    main()