# author: JustBeast
def isPrime(n):
	for x in range (2, n/2 + 1): #it is n/2 + 1 because of the range function
		if n%x == 0:
			return False
	return True
prime=[]
def goldbach(x):
	for x in range(2, x):
		if isPrime(x) == True:
			prime.append(x)
	for i in prime:
		evaluate=x-i
		if isPrime(evaluate) == True:
			print i + "and" + evaluate
			return True
	return False
def inathousand():
	for u in range(1, 1000):
		if goldbach(u) == False:
			print u
			return "Found it"
			
	
		