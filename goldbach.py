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
for 
		