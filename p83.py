# uses the same idea as p82
import heapq, sys

# Input
sys.stdin = open("Data/p083_matrix.txt", "r")
size = 80
mat = [map(int, raw_input().split(",")) for i in xrange(size)]

# the paths stand for:
paths = [(-1, 0), # move left
		(1, 0), # move right
		(0, 1), # move down
		(0, -1)] # move up

Q = [(mat[0][0], (0, 0)) for i in xrange(size)]
heapq.heapify(Q)

# set up the djikstras and distances
dists = [[99999999 for i in xrange(size)] for j in xrange(size)]
dists[0][0] = mat[0][0]

while Q:
	dist, (y, x) = heapq.heappop(Q)
	for dx, dy in paths:
		if 0<= x+dx < size and 0<= y+dy < size:
			if x+dx == size-1 and y+dy == size-1: # reached the end
				Q = []
				print dist + mat[y+dy][x+dx]
			elif dists[y+dy][x+dx] > dist + mat[y+dy][x+dx]:
				dists[y+dy][x+dx] = dist + mat[y+dy][x+dx]
				heapq.heappush(Q, (dist + mat[y+dy][x+dx], (y+dy, x+dx)))
