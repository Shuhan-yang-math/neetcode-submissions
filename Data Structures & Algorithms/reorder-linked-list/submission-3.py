# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow=head
        fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None
        prev=None
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node
        first=head
        second=prev
        while second:
            next_first=first.next
            next_second=second.next
            first.next=second
            second.next=next_first
            first=next_first
            second=next_second


        