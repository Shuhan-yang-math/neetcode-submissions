# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next and n==1:
            return None
        A={}
        i=0
        while head:
            A[i]=head
            head=head.next
            i=i+1
        if i-n==0:
            return A[1]
        if i-n+1 in A:
            A[i-n-1].next=A[i-n+1]
        else:
            A[i-n-1].next=None
        return A[0]
