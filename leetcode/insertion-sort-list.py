# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p, c = head, head.next
        while c:
            if c.val >= p.val:
                p, c = c, c.next
                continue
            tmp = dummy
            while tmp.next.val <= c.val:
                tmp = tmp.next
            p.next = c.next
            c.next = tmp.next
            tmp.next = c
            c = p.next
        return dummy.next