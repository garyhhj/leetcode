#leetcode #238
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = [1] * len(nums)
        l = [1] * len(nums)

        l[0] = nums[0]
        for i in range(1, len(nums), 1): 
            l[i] = nums[i] * l[i - 1]

        
        r[len(nums) - 1]  = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1): 
            r[i] = nums[i] * r[i + 1]
        
        ans = [1] * len(nums)
        for i in range(0, len(nums), 1): 
            ans[i] = (l[i - 1] if i - 1 >= 0 else 1) * \
            (r[i + 1] if (i + 1) < len(nums) else 1) 

        return ans