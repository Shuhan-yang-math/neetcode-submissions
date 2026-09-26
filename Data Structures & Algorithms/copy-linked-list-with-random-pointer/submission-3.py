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
        if not head:
            return None
        a=head
        A={}
        while a:
            A[a]=Node(a.val)
            a=a.next
        b=head
        while b:
            if not b.next:
                A[b].next=None
            else:
                A[b].next=A[b.next]
            if not b.random:
                A[b].random=None
            else:
                A[b].random=A[b.random]
            b=b.next
        return A[head]

        