collatz-conjecture
==================
def collatz(x):
	count= 0
	while x > 1:
		if x % 2== 0:
			x = x/2
			count += 1
		else:
			x = x*3 + 1
			count += 1
	return count
	
collatz(478)

def greatest():
	m=0
	v=0
	for x in range(1, 1001):
		if collatz(x)> m:
			m=collatz(x)
			v=x
	print m
	print v
	
greatest()
x=9
x+=5
print x
print collatz(178)
	
#this function finds how which number has the greatest chain sequence until it reaches 1 and finds how long that sequence is (all based on the collatz conjecture!!!!!!! :) :) :) :) :) :) :) :) :) :) 

:)
		

			

		
		

			
