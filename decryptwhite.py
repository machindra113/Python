#!/usr/bin/python3

import sys

def main():
	fh = open(sys.argv[1], 'r')
	res = fh.readlines()
	fin = ''.join(res)
	str1 = fin.replace("\t", "1")
	str2 = str1.replace(" ", "0")
	strf = ''.join(str2)
	print(strf)

	
	fh.close()
if __name__ == '__main__':
	main()
