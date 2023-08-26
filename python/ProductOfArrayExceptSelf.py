class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums); 

        prev = nums[0]
        for i in range(1, len(nums), 1): 
            ans[i] *= prev
            prev *= nums[i]

        nxt = nums[len(nums) - 1]    
        for i in range(len(nums) - 2, -1, -1): 
            ans[i] *= nxt
            nxt *= nums[i]
        
        return ans