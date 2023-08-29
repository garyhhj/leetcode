#leetcode 155
class MinStack:
    priority = []
    stack = []

    def __init__(self):
        self.priority.clear()
        self.stack.clear()
        return 

    def push(self, val: int) -> None:
        self.stack.append(val)

        currMinIndex = 0
        if len(self.priority) != 0: 
            currMinIndex = self.priority[-1]
        pNewIndex = len(self.stack) - 1

        if self.stack[currMinIndex] < self.stack[pNewIndex]: 
            self.priority.append(currMinIndex)
        else: 
            self.priority.append(pNewIndex)

    def pop(self) -> None:
        self.priority.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.stack[self.priority[len(self.priority) - 1]]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()