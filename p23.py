size = 28123 
sieve = [0, 1] + [1 for i in xrange(size-1)]

for i in xrange(2, size, 2):
	sieve[i] += 1

for i in xrange(3, size):
	for j in xrange(i+i, size, i):
		sieve[j] += i

cnt = 0
lst = []
for i in xrange(size+1):
	if i < sieve[i]:
		lst.append(i)

total = set()
for i in xrange(len(lst)):
	for j in xrange(len(lst)):
		if lst[i] + lst[j] <= size:
			total.add(lst[i] + lst[j])

print size*(size+1)/2 - sum(list(total))