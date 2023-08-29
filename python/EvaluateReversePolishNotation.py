#leetcode #150
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            #if token is symbol 
            if token == '+' or token == '-' or token == '*' or token == '/': 
                lhs = int(stack[len(stack) - 2])
                rhs = int(stack[len(stack) - 1])

                if token == '+': 
                    stack[len(stack) - 2] = lhs + rhs
                elif token == '-': 
                    stack[len(stack) - 2] = lhs - rhs
                elif token == '*': 
                    stack[len(stack) - 2] = lhs * rhs
                elif token == '/': 
                    stack[len(stack) - 2] = int(lhs / rhs)
                stack.pop()
            else: 
                stack.append(token)

        return int(stack[0])