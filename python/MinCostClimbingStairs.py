#leetcode #746
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [inf] * (len(cost) + 1)
        dp[0], dp[1] = 0, 0

        n = len(cost)
        for i in range(0, n - 1, 1): 
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])
        dp[n] = min(dp[n], dp[n - 1] + cost[n - 1])

        return dp[n]