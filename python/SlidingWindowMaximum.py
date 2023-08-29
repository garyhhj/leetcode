#leetcode #239 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        que = collections.deque()

        for i in range(0, k, 1): 
            while len(que) > 0 and que[-1] < nums[i]: 
                que.pop()
            que.append(nums[i])
            
        for i in range(0, len(nums) - k, 1):
            #add max of que to result 
            res.append(que[0])
            #remove old element 
            if que[0] == nums[i]: 
                que.popleft()

            #remove smaller elements in que 
            while len(que) > 0 and que[-1] < nums[i + k]: 
                que.pop()
            que.append(nums[i + k])


        res.append(que[0])
        return res