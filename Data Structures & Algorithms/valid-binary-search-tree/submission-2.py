# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        arr = []

        def inOrder(root):
            if not root:
                return 

            inOrder(root.left)

            arr.append(root.val)

            inOrder(root.right)

            return 
        
        inOrder(root)
        
        for i in range(len(arr)):

            if i+1 < len(arr) and arr[i] >= arr[i+1]:
                return False
        
        return True

        


        