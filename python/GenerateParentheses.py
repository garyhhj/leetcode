#leetcode #22
def solve(delimiter : int, n : int, used : int, curr : str, ans : list) -> None: 
    if delimiter == n: 
        if len(curr) == 2*n: 
            ans.append(curr)
        return 
    
    l = len(curr)
    curr += "("
    for i in range(0, delimiter - used + 2, 1): 
        _curr = curr 
        for j in range(0, i, 1): 
            _curr += ")"
        solve(delimiter + 1, n, used + i, _curr, ans)

    curr = curr[0: l]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        solve(0, n, 0, "", ans)
        return ans 