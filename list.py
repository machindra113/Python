
list=[1,4,7,10,15,20,78]

for number in list:

	if number%2==0:
		print (f"{number} is even")
	else:
		print (f"{number} is odd")
	


for c in (10,25,30) :
	
	if c%10==0:
		print (f"{c} is divisible by 10")
	else:
		print (f"{c} is not divisible by 10")	
print ("For loop in dictionary")

dict = {1:"Tinku",2:"pinky", 3:"gabbar"}
for d in dict:
	print (d)

for d in dict.values():
	print (d)
