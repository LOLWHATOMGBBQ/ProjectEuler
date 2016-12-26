# we call start from a source x and end at
# a ending y. We say that x connects to everything
# in the first column and everything in the last 
# column connects to y, where all connection have a 
# a weight of 0. We can then perform djikstras algorithm
# on the graph, starting from x, going to y.

import heapq, sys

sys.stdin = open("Data/p082_matrix.txt", "r")
size = 80
# the paths stand for:
paths = [(1, 0), # move right
		(0, 1), # move down
		(0, -1)] # move up
mat = [map(int, raw_input().split(",")) for i in xrange(size)]

Q = [(mat[i][0], (i, 0)) for i in xrange(size)]
heapq.heapify(Q)
tot_dist = 0
dists = [[99999999 for i in xrange(size)] for j in xrange(size)]
while Q:
	dist, (y, x) = heapq.heappop(Q)
	for dx, dy in paths:
		if 0<= x+dx < size and 0<= y+dy < size:
			if x+dx == size-1:
				Q = []
				tot_dist = dist + mat[y+dy][x+dx]
			elif dists[y+dy][x+dx] > dist + mat[y+dy][x+dx]:
				dists[y+dy][x+dx] = dist + mat[y+dy][x+dx]
				heapq.heappush(Q, (dist + mat[y+dy][x+dx], (y+dy, x+dx)))

print tot_dist
