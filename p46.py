# Sieve
upper = 100000
nums = [False, False] + [True for i in xrange(upper-1)]
for i in xrange(4, upper+1, 2):
	nums[i] = False
for i in xrange(3, int(upper**0.5) + 1, 2):
	for j in xrange(i+i, upper+1, i):
		nums[j] = False

# generates all of the squares and primes
squares = [2* i**2 for i in xrange(1, int(upper**0.5)+1)]
primes = []
for i in xrange(upper+1): 
	if nums[i]: 
		primes.append(i)
# goes through each pair of primes and squares and marks
# their sum as composable
for i in squares:
	for j in primes:
		if i+j <= upper:
			nums[i+j] = True
# goes through the list of numbers and finds the first odd
# composite number that cannot be made
for i in xrange(2, upper+1):
	if i%2 and not nums[i]:
		print i
		break