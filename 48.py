# simple modular exponentiation

MOD = 10**10
total = 0
for i in xrange(1, 1001):
	total += pow(i, i, MOD)
	total %= MOD
print total

# the one-liner solution
# print sum([pow(i, i, 10**10) for i in xrange(1, 1001)])%10**10