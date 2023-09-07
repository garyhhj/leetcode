#leetcode #1046
def smash(s1: int, s2: int) -> int: 
    if s1 == s2: 
        return 0
    else: 
        return s2 - s1

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1: 
            res = smash(stones[-2], stones[-1])
            stones.pop()
            if res == 0: 
                stones.pop()
            else: 
                stones[-1] = res
            stones.sort()
        return stones[0] if len(stones) == 1 else 0