#leetcode #202
def nextState(n : int) -> int: 
    temp = 0
    while n != 0:
        temp += (n % 10) ** 2 
        n //= 10
    n = temp
    return temp

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, nextState(n)

        while slow != fast: 
            slow = nextState(slow)
            fast = nextState(fast)
            fast = nextState(fast)
        
        return True if fast == 1 else False 

