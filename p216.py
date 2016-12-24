size = 50*10**6
sieve = [False, False] + [True for i in xrange(size)]

for i in xrange(4, size, 2):
	sieve[i] = False

for i in xrange(3, int(size**0.5)+1):
	for j in xrange(i+i, size, i):
		sieve[j] = False

a = set([i*i for i in xrange(7071)])
cnt = -1
for i in xrange(size):
	if sieve[i] and (i+1)/2 in a:
		#print i
		cnt += 1

print cnt