# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a=head
        if not a or not a.next:
            return False
        b=head
        while b.next and b.next.next:
            if a.next==b.next.next:
                return True
            else:
                a=a.next
                b=b.next.next
        return False
