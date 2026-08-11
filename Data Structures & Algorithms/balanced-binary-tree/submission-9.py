# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0

            LH = dfs(node.left)
            RH = dfs(node.right)

            if abs(RH-LH) > 1:
                return -1
            
            if RH == -1 or LH == -1:
                return -1
            
            return 1 + max(LH,RH)
        
        return dfs(root) != -1