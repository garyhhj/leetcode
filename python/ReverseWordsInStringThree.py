#leetcode #557

'''
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        curr = ""
        for i in range(0, len(s), 1): 
            if s[i] == " ": 
                res += curr[::-1]
                curr = ""
                res += " "
                continue
            curr +=  s[i]
        return res + curr[::-1]
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = lambda word : word[::-1]
        return " ".join(map(reverse, s.split()))
        