# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        temp = head.next#this may cha
        a, b = head, head.next
        while b and b.next:
            a.next = b.next
            a = b.next
            b.next = a.next
            b = a.next
        a.next = temp
        return head