# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root):
            if not root:
                return 0
            
            HL,HR = height(root.left) , height(root.right)

            if abs(HL - HR) > 1:
                return -1
            
            if HL == -1 or HR == -1:
                return -1
                
            return 1 + max(HL,HR)
        
        return height(root) != -1 

            
            
            

        
        