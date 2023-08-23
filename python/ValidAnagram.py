#leetcode #242
def getFreq(freq: {}, s: str) -> None: 
    for i in s: 
        freq[i] = 1 + freq.get(i, 0)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS, freqT = {}, {}
        getFreq(freqS, s)
        getFreq(freqT, t)
        return freqS == freqT
