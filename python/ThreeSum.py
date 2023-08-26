#leetcode #15
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numIndex = {} #num -> index
        for i in range(0, len(nums), 1): 
            numIndex[nums[i]] = i 

        res = set()
        for i in range(0, len(nums), 1): 
            for j in range(i + 1, len(nums), 1):
                target = 0 - nums[i] - nums[j]
                if target in numIndex and numIndex[target] > j:
                    res.add(tuple(sorted([nums[i], nums[j], nums[numIndex[target]]])))

        return res
