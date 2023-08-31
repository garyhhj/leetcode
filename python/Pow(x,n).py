#leetcode #50
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        neg = True if n < 0 else False  
        n = abs(n)

        curr = x 
        while n != 0: 
            if n % 2 == 1: 
                res *= curr 
            curr *= curr   
            n //= 2 

        return 1 / res if neg else res 