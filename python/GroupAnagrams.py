#leetcode #49
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)

        for str in strs: 
            key = [0] * 26 
            for c in str: 
                key[ord(c) - ord('a')] += 1; 
            res[tuple(key)].append(str)

        return res.values(); 


            