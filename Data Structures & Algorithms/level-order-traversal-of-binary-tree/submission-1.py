# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        while not root:
            return []
        B=[]
        A=deque([root])
        while A:
            size=len(A)
            D=[]
            for i in range(size):
                c=A.popleft()
                D.append(c.val)
                if c.left:
                    A.append(c.left)
                if c.right:
                    A.append(c.right)
            B.append(D)
        return B
