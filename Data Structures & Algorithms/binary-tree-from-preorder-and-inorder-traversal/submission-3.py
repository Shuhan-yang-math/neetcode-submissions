# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        place={val:i for i,val in enumerate(inorder)}
        preindex=0
        def build(left,right):
            nonlocal preindex
            if left>right:
                return None
            a=preorder[preindex]
            node=TreeNode(a)
            s=place[a]
            preindex=preindex+1
            node.left=build(left,s-1)
            node.right=build(s+1,right)
            return node
        return build(0,len(preorder)-1)
