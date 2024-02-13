# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        ptr = dummy
        cur = head
        while cur:
            if cur.val < x:
                temp = ListNode(val=cur.val)
                ptr.next = temp
                ptr = ptr.next
            cur = cur.next
        cur = head
        while cur:
            if cur.val >= x:
                temp = ListNode(val=cur.val)
                ptr.next = temp
                ptr = ptr.next
            cur = cur.next
        
        return dummy.next
