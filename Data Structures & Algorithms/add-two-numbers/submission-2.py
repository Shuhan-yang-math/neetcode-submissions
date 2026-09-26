# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1=l1
        x2=l2
        c=0
        d=0
        dummy=ListNode(0)
        e=dummy
        while x1 and x2:
            c=(x1.val+x2.val+d)%10
            d=(x1.val+x2.val+d)//10
            e.next=ListNode(c)
            e=e.next
            x1=x1.next
            x2=x2.next
        while x1:
            c=(x1.val+d)%10
            d=(x1.val+d)//10
            e.next=ListNode(c)
            e=e.next
            x1=x1.next
        while x2:
            c=(x2.val+d)%10
            d=(x2.val+d)//10
            e.next=ListNode(c)
            e=e.next
            x2=x2.next
        if d!=0:
            e.next=ListNode(d)
        return dummy.next

            

        