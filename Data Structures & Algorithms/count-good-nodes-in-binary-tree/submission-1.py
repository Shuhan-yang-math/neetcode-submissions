# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def find(node,p):
            if not node:
                return 0
            count=0
            if node.val>=p:
                count=1
            p1=max(p,node.val)
            return (count+find(node.left,p1)+find(node.right,p1))
        return find(root,-float("inf"))

        