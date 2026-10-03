"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        copies={}
        def d(old):
            if old in copies:
                return copies[old]
            new=Node(old.val)
            copies[old]=new
            for neighbor in old.neighbors:
                new.neighbors.append(d(neighbor))
            return new
        return d(node)
        