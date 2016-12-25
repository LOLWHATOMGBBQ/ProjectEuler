# the equation must satisfy
# a x b = c
# so there are at least 2 digits on the left side and the number of
# digits on the right must be at least 3
# so we only need to search up to (9876543)^0.5

largest = 3143#2.6967718823908194707255836796#4000
compare = map(str, range(1, 10))
nums = set()
for i in xrange(1, largest):
	for j in xrange(1, largest):
		if sorted(list(str(i) + str(j) + str(i*j))) == compare:
			nums.add(i*j)
print sum(nums)