#leetcode #567
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        #just check and compare hash
        freq1 = [0] * 26
        for c in s1: 
            freq1[ord(c) - ord('a')] += 1 
        
        freq2 = [0] * 26 
        for i in range(0, len(s1), 1): 
            freq2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(0, len(s2) - len(s1), 1):
            if freq1 == freq2: 
                return True 
            freq2[ord(s2[i]) - ord('a')] -= 1 
            freq2[ord(s2[i + len(s1)]) - ord('a')] += 1
        if freq1 == freq2: 
            return True 

        return False