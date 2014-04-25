# author: JustBeast
def isPrime(n):
	for x in range (2, n/2 + 1): #it is n/2 + 1 because of the range function
		if n%x == 0:
			return False
	return True

def average():
	x=[]
	for i in range (1,3001):
		if isPrime(i) == True:
			x.append(i)
	lastprime=0
	differences=[]
	for a in x:
		l=a-lastprime
		differences.append(l)
		lastprime=a
	return sum(differences)/len(differences)
print average()