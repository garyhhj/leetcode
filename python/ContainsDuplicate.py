#leetcode #217
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for i in nums: 
            if i in freq: 
                return True
            freq[i] = 1
        return False