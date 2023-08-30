#leetcode #53
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = nums[0]
        for i in range(1, len(nums), 1): 
            prev = max(nums[i], nums[i] + prev)
            res = max(res, prev)

        return res 
        