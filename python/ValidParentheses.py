#leetcode #20
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s: 
            stack.append(bracket) 
            #deleting matching bracket 
            while len(stack) >= 2: 
                currBracket = stack[len(stack) - 1]
                prevBracket = stack[len(stack) - 2]
                if (
                    (prevBracket == '(' and currBracket == ')' ) or
                    (prevBracket == '[' and currBracket == ']' ) or 
                    (prevBracket == '{' and currBracket == '}') 
                    ): 
                    stack.pop()
                    stack.pop()
                else: 
                    break 

        return len(stack) == 0    

                