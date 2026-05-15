# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.Max = 0

        def height(root):
            if not root:
                return 0

            leftH = height(root.left)
            rightH = height(root.right)

            self.Max = max(self.Max, (leftH + rightH))

            return 1 + max(leftH,rightH)
            
        height(root)

        return (self.Max)
        