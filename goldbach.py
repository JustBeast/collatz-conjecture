# author: JustBeast
def isPrime(n):
	for x in range (2, n/2 + 1): #it is n/2 + 1 because of the range function
		if n%x == 0:
			return False
	return True

def goldbach(x):
	for i in range(2, x):
		if isPrime(i) == True:
			evaluate=x-i
			#finds prime numbers and stores just uses them straight away.  it does not store it in a list.
			if isPrime(evaluate) == True:
				print str(i) + " + " + str(evaluate) + " = " + str(x)
				return True
			#subtracts prime numbers from initial number to see if diff == a prime number 

	return False

def inathousand():
	for u in range(4, 1000):
		if goldbach(u) == False:
			print u
			return "Found it"
def goldbach_triples(x):
	for i in range(2, x):
		if isPrime(i) == True:
			evaluate=x-i
			if goldbach(evaluate) == True:
				print str(i)
			return True
goldbach_triples(3458)
			

	
		