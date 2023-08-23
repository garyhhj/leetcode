#leetcode #1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        for i in range(len(nums)): 
            numIndex[nums[i]] = i
        
        for i in range(len(nums)):
            otherTarget = target - nums[i]
            if otherTarget in numIndex and i != numIndex[otherTarget]: 
                return [i, numIndex[otherTarget]]

        return [-1, -1] #will never reach here 