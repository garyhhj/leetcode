#leetcode #543

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self): 
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode]) -> int: 
            if root is None: 
                return 0
            
            max_right, max_left = helper(root.right), helper(root.left)
            self.res = max(self.res, max_right + max_left)
            return max(max_right, max_left) + 1

        helper(root)
        return self.res