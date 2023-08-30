#leetcode #739
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        indexes, stack = [], []

        res = [0] * len(temperatures)
        for i in range(0, len(temperatures), 1): 
            while len(stack) > 0 and stack[-1] < temperatures[i]: 
                res[indexes[-1]] = i - indexes[-1] 
                indexes.pop() 
                stack.pop()
            indexes.append(i)
            stack.append(temperatures[i])
        
        return res
