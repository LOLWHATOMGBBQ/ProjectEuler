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

types = set()
for i in xrange(10):
	for j in xrange(10):
		for k in xrange(10):
			for l in xrange(10):
				good = set()
				for m in perm([i,j,k,l]):
					num = int("".join(map(str, m)))
					if nums[num] and num >= 1000:
						good.add(num)
				if len(good) >= 3:
					for m in comb(good, 3):
						lst = sorted(m[:3])
						if lst[0] - lst[1] == lst[1] - lst[2]:
							types.add("".join(map(str,lst)))
for i in types:
	print i
							
