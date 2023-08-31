#leetcode #55
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 1

        for i in range(0, len(nums) - 1, 1): 
            if curr == 0: 
                break
            curr -= 1 
            curr = max(curr, nums[i])

        return True if curr != 0 else False 
            