# Similar to knapsack dp, uses the same ideas

money = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [[0 for i in xrange(money+1)] for j in xrange(len(coins))]
dp[0][0] = 1
for i in xrange(coins[0], money+1, coins[0]):
	dp[0][i] += 1
for i in xrange(1, len(coins)):
	for j in xrange(money+1):
		if coins[i] <= j:
			dp[i][j] += dp[i][j-coins[i]] + dp[i-1][j]
		else:
			dp[i][j] += dp[i-1][j]

print dp[-1][money]