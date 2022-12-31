def main():
    ls = []
    num = int(input("Enter the number to reverse "))
    while num > 0:
        r = int(num%10)
        num = int(num/10)
        ls.append(r)
        revnum = ''.join([str(i) for i in ls])
    print("Reversed string is ", revnum)
if __name__ == "__main__":
    print("Reverse a given integer...")
    main()