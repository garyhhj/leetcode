#leetcode #125
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return re.sub('[\W_]+', '', s).lower() == re.sub('[\W_]+', '', s).lower()[::-1]
