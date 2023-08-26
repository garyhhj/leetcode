#leetcode #128
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elementIndex = {}
        for i in range(0, len(nums), 1): 
            elementIndex[nums[i]] = i

        elementConsecutive = {}
        res = 0
        for num in nums: 
            consecutive = 1
            _num = num 
            while _num + 1 in elementIndex: 
                if _num + 1 in elementConsecutive: 
                    consecutive += elementConsecutive[_num + 1]
                    break 
                _num += 1 
                consecutive += 1 
            elementConsecutive[num] = max(elementConsecutive.get(num, 1), consecutive)
            res = max(res, consecutive)

        return res  