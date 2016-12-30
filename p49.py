import itertools
comb = itertools.combinations
perm = itertools.permutations

# Sieve
upper = 1000000
nums = [False, False] + [True for i in xrange(upper-1)]
for i in xrange(4, upper+1, 2):
	nums[i] = False
for i in xrange(3, int(upper**0.5) + 1, 2):
	for j in xrange(i+i, upper+1, i):
		nums[j] = False

# Brute forces through every single possible four digit number
types = set()
for i in xrange(10):
	for j in xrange(10):
		for k in xrange(10):
			for l in xrange(10):
				# some optimization
				if sorted(list(set([i,j,k,l]))) == sorted([i,j,k,l]):
					good = set()
					# iterates through each permutation of the numbers
					# and makes sure that the concatenation of the numbers
					# is a 4 digit number (greater or equal to 1000)
					for m in perm("".join([i,j,k,l])):
						num = int(m)
						# checks if the number is prime and if its a 4 digit
						# number
						if nums[num] and num >= 1000: 
							good.add(num)
					# checks if there are at least 3 primes with the digits
					# i,j,k,l in some order 
					if len(good) >= 3:
						for m in comb(good, 3):
							lst = sorted(m[:3])
							# checks if its an arithmetic sequence
							if lst[0] - lst[1] == lst[1] - lst[2]:
								# concatenates the numbers and adds them to a set
								types.add("".join(map(str,lst)))
# the two concatenated strings
for i in types:
	print i
							
