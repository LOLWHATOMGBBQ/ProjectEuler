import sys

# simple top down dynamic programming
# takes the maximum of the top and the path from the right

sys.stdin = open("Data/p081_matrix.txt", 'r')
size = 80
mat = [map(int, raw_input().split(",")) for i in xrange(size)]

for i in xrange(1, size):
	mat[0][i] += mat[0][i-1]
	mat[i][0] += mat[i-1][0]
for i in xrange(1, size):
	for j in xrange(1, size):
		mat[i][j] += min(mat[i-1][j], mat[i][j-1])
print mat[-1][-1]
