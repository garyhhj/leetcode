#leetcode #167
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1;
        while l < r: 
            currSum = numbers[l] + numbers[r]
            if currSum == target: 
                return [l + 1, r + 1]
            
            if currSum < target: 
                l += 1 
            else: # currSum > target
                r -= 1 
        
        #never reached 
        return [-1, -1]