# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        deq = collections.deque()
        deq.append(root)

        while deq:
            qLen = len(deq)
            level = []

            for i in range(len(deq)):
                node = deq.popleft()
                if node:
                    level.append(node.val)
                    deq.append(node.left)
                    deq.append(node.right)
            if level:
                res.append(level)
        
        return res

            
            
            
