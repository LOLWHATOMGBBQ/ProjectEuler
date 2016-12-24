n = 500000
tot = 0
for a in xrange(10):
	for b in xrange(10):
		for c in xrange(10):
			for d in xrange(10):
				for e in xrange(10):
					for f in xrange(10):
						num = int("%d%d%d%d%d%d"%(a, b, c, d, e, f))
						if sum(map(lambda x: x**5, [a, b, c, d, e, f])) == num:
							tot += num
print tot