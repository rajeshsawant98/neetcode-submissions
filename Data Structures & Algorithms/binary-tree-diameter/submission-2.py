# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.Diameter = 0

        def dfs(root):
            if not root:
                return 0
            
            LH = dfs(root.left)
            RH = dfs(root.right)

            self.Diameter = max(self.Diameter, LH+RH)

            return 1 + max(LH,RH)

        dfs(root)

        return self.Diameter