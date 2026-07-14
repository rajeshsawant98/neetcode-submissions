# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0
            
            LH = dfs(root.left)
            RH = dfs(root.right)

            if LH ==-1 or RH == -1 or abs(LH-RH) > 1:
                return -1
        
            return 1 + max(LH,RH)
        
        return dfs(root) != -1
