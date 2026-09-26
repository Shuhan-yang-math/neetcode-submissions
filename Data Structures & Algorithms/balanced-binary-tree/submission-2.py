# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        a=0
        def length(node):
            nonlocal a
            if not node:
                return 0
            left=length(node.left)
            right=length(node.right)
            if abs(left-right)>=2:
                a=-1
            return 1+max(left,right)
        length(root)
        return a==0
        