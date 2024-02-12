# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        dummy = ListNode(next=head)
        temp = dummy
        for _ in range(left - 1):
            temp = temp.next
        a, b = temp.next, temp.next.next
        head = b.next
        last = temp.next
        for i in range(right - left):
            b.next = a
            if i != right - left - 1:
                a, b = b, head
                head = head.next
        temp.next = b
        last.next = head
        return dummy.next
        
