#leetcode #347
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: 
            freq[num] = 1 if num not in freq else freq[num] + 1
        
        occurence = [[] for i in range(len(nums) + 1)]

        for key in freq: 
            occurence[freq[key]].append(key) 

        ans = []
        print(occurence)
        for i in range(len(nums), 0, -1): 
            if len(occurence[i]) != 0:
                for num in occurence[i]: 
                    if len(ans) == k: 
                        break
                    ans.append(num)
                     
        return ans