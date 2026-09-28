# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        A=deque([root])
        result=[]
        while A:
            c=len(A)
            for i in range(c):
                d=A.popleft()
                if d.left:
                    A.append(d.left)
                if d.right:
                    A.append(d.right)
                if i==c-1:
                    result.append(d.val)
        return result
        