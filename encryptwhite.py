#!/usr/bin/python3

import sys

def main():
	st = sys.argv[1]
	fh = open('200.txt', 'w')
	bin = ''.join(format(ord(x), 'b') for x in st)
	str1 = bin.replace("0", " ")
	str2 = str1.replace("1", "\t")
	fh.write(str2)
	fh.close()
if __name__ == '__main__':
	main()
