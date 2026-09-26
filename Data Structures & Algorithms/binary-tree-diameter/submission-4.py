# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def length(node):
            nonlocal ans
            if not node:
                return 0
            left=length(node.left)
            right=length(node.right)
            ans=max(ans,left+right)
            return 1+max(left,right)
        length(root)
        return ans

        