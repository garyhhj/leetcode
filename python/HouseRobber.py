#leetcode #198
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        n = len(nums)
        for i in range(0, n, 1):
            dp[i] = nums[i] 
            if i - 2 >= 0: 
                dp[i] = max(dp[i], nums[i] + dp[i - 2])
            if i - 3 >= 0: 
                dp[i] = max(dp[i], nums[i] + dp[i - 3])

        res = dp[n - 1]
        if n > 1: 
            res = max(res, dp[n - 2])
        return res