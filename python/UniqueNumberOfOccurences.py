#leetcode #1207
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        occurence = {}
        for k,v in freq.items(): 
            if v in occurence: 
                return False 
            occurence[v] = True
        return True 
        