#leetcode #3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        l, r = 0, 0

        freq = {}
        while r < len(s): 
            if s[r] not in freq: 
                freq[s[r]] = 0 
            freq[s[r]] += 1

            while freq[s[r]] == 2: 
                freq[s[l]] -= 1 
                l += 1 
            
            ans = max(ans, r - l + 1)
            r += 1 
        
        return ans 