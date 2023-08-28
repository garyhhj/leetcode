#leetcode #121
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        highest = 0
        for i in range(len(prices) - 1, -1, -1): 
            ans = max(ans, highest - prices[i]) 
            highest = max(highest, prices[i])
        return ans