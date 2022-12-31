#!/usr/bin/python3

import re

class reg:
	def __init__(self, str):
		self.teststr = str
	def convert(self):
		#Regex 3
		fstr = re.findall(r'[A-Z][a-z]*', self.teststr)
		if (fstr):
			print("Whitespace found")
			#for i in range(len(fstr)):
      		#		fstr[i]=fstr[i][0].lower()+fstr[i][1:]
			print("The string formed is : ", (' '.join(fstr)).lower())
		else:
			print("No whitespaces")
		return "The string used is : {}".format(self.teststr)

	def zcheck(self):
		#Regex 2
		if (re.search(r'z0\b', self.teststr) or re.search(r'zd+', self.teststr)):
			return True
		else:
			return False

def main():
	string = reg('ILoveBatman')
	print(string.convert())

	#string = reg('zb')
	#print(string.zcheck())

if __name__ == '__main__':
	main()
