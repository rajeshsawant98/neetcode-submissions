"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None : None}

        curr = head 

        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next

        curr2 = head

        while curr2:
            node = oldToNew[curr2]
            node.next = oldToNew[curr2.next]
            node.random = oldToNew[curr2.random]
            curr2 = curr2.next

        
        return oldToNew[head]