#leetcode #239
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #use a segment tree for (n + k)logn time complexity and O(n) space 

        #initializing segment tree 
        segmentTree = [0] * (2 * len(nums))
        for i in range(len(nums), len(segmentTree), 1): 
            segmentTree[i] = nums[i - len(nums)]
        for  i in range(len(nums) - 1, 0, -1): 
            segmentTree[i] = -inf 
        
        for i in range(len(segmentTree) - 1, 0, -1): 
            segmentTree[i // 2] = max(segmentTree[i // 2], segmentTree[i])

        # search range [l, r)
        def query(l : int, r : int): 
            l += len(nums)
            r += len(nums)
            res = -inf 
            while l < r:
                if l % 2 == 1: 
                    res = max(res, segmentTree[l])
                    l += 1
                if r % 2 == 1: 
                    r -= 1
                    res = max(res, segmentTree[r])

                l //= 2
                r //= 2 
            return res 

        #range query 
        res = []
        for i in range(0, len(nums) - k + 1, 1): 
            res.append(query(i, i + k))
        return res 



