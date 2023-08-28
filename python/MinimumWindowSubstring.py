#leetcode #76
def valid(freqS : list, freqT : list) -> bool: 
    for i in range(0, len(freqS), 1): 
        if freqS[i] < freqT[i]: 
            return False
    return True 

def increment(freq : list, c : str) -> None: 
    if ord('a') <= ord(c) and ord(c) <= ord('z'): 
        freq[ord(c) - ord('a')] += 1
    else : 
        freq[ord(c) - ord('A') + 26] += 1

def decrement(freq : list, c : str) -> None: 
    if ord('a') <= ord(c) and ord(c) <= ord('z'): 
        freq[ord(c) - ord('a')] -= 1
    else : 
        freq[ord(c) - ord('A') + 26] -= 1

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqS, freqT = [0] * 52, [0] * 52

        #hash both freq
        for c in s: 
            increment(freqS, c)
        for c in t: 
            increment(freqT, c)

        #check if solution exists 
        if not valid(freqS, freqT): 
            return ""
        
        #clear hash for s 
        freqS = [0 for i in range(52)]
        increment(freqS, s[0])
        
        ans = len(s)
        _l, _r = 0, len(s) - 1 

        l, r = 0, 0 #inclusive 
        while r < len(s):
            validRL = valid(freqS, freqT) 
            if r - l + 1 < ans and validRL: 
                ans = r - l + 1 
                _l, _r = l, r 
            
            print("r l: ", l, r, validRL)
            if validRL: 
                decrement(freqS, s[l])
                l += 1 

            else: 
                r += 1 
                if r == len(s): 
                    break
                increment(freqS, s[r])
        if r - l + 1 < ans and valid(freqS, freqT): 
            ans = r - l + 1 
            _l, _r = l, r
        
        return s[_l : _r + 1]

        
