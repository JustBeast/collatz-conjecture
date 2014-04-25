# author: JustBeast
def isPrime(n):
	for x in range (2, n/2 + 1): #it is n/2 + 1 because of the range function
		if n%x == 0:
			return False
	return True

def average():
	for i in range (1,1001):
		x=[]
		if isPrime(i) == True:
			x.append(i)
	lastprime=0
	differences=[]
	for a in x:
		a - lastprime=l
		differences.append(l)
		a=lastprime
	sum(differences)/len(differences)
print average()
		