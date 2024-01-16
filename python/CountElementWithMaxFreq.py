#leetcode #3005

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = [0] * 101
        for num in nums: 
            freq[num] += 1
        
        total_freq = 0
        max_freq = 0
        for i in range(0, 101): 
            if freq[i] > max_freq: 
                total_freq = freq[i]
                max_freq = freq[i]
            elif freq[i] == max_freq: 
                total_freq += freq[i]
            
        return total_freq
                
        