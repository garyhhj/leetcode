#leetcode #202
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = {}

        while n != 1:
            if n in visited: 
                return False
            visited[n] = True 

            temp = 0
            while n != 0: 
                temp += (n % 10) * (n % 10)
                n //= 10
            n = temp

        return True 
