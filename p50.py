import bisect

upper = 1000000
nums = [False, False] + [True for i in xrange(upper-1)]
for i in xrange(4, upper+1, 2):
	nums[i] = False
for i in xrange(3, int(upper**0.5) + 1, 2):
	for j in xrange(i+i, upper+1, i):
		nums[j] = False
primes = []
for i in xrange(upper+1):
	if nums[i]:
		primes.append(i)

prime_sum = [0 for i in xrange(len(primes)+1)]
for i in xrange(len(primes)):
	prime_sum[i+1] = primes[i] + prime_sum[i]

total = 0

for i in xrange(len(primes)):
	for j in xrange(i-total-1, -1, -1):
		temp = prime_sum[i] = prime_sum[j]
		if temp > upper:
			break
		if bisect.bisect_right(primes, temp) >= 0:
			total = i - j
			final = prime_sum[i] = prime_sum[j]
print final 
