#leetcode #424
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = [0] * 26
        for i in range(0, k, 1): 
            freq[ord(s[i]) - ord('A')] += 1

        ans = k
        l, r = 0, k - 1
        while r < len(s): 

            if k >= r - l + 1 - max(freq): 
                ans = max(ans, r - l + 1)
                r += 1
                if r == len(s): 
                    break
                freq[ord(s[r]) - ord('A')] += 1
            
            else: 
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1 
            
        return ans 
            
            