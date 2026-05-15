# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):

            if not node:

                return 0

            leftH = height(node.left)

            rightH = height(node.right)

            # subtree already unbalanced

            if leftH == -1 or rightH == -1:

                return -1

            # current node unbalanced

            if abs(leftH - rightH) > 1:

                return -1

            return 1 + max(leftH, rightH)

        return height(root) != -1

