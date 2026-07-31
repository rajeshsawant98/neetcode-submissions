# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []

        q = collections.deque([root] if root else [])

        while q:

            level = []
            qlen = len(q)

            for _ in range(qlen):

                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level = reversed(level) if len(res) % 2 == 1 else level
            res.append(level)
        

        return res
        