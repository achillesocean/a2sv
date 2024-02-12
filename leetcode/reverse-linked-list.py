# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        if not head.next: return head
        a = head
        b = head.next
        head.next = None
        head = b.next
        while head:
            b.next = a
            a, b = b, head
            head = head.next
        b.next = a
        return b
        