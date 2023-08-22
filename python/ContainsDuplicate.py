class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #we can use a map and map numbers and check the output of the map 
        freq = {}
        for i in nums: 
            if i in freq: 
                return True
            freq[i] = 1
        return False