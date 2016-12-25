upper = 10
fact = range(upper)
fact[0] = 1
for i in xrange(1,upper):
	fact[i] *= fact[i-1]

numbers = []
# we notice that the largest factorial for
# the single digits is 9! = 362880
# thus, the largest number could have 7 digits
# (9!)*7 is a 7 digit number
for i in xrange(2540160): # this number is 7x9!
	# converts the number into list form
	num = map(int, list(str(i)))
	# take the total of the factorials
	total = sum(map(lambda x: fact[x], num))
	if total == i:
		numbers.append(i)
print numbers
print sum(numbers)
# the numbers are [1, 2, 145, 40585]
# and the sum is 40733
# however, we dont include 1! = 1 and 2! = 2
# so the sum is 40730