# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        keep = ListNode(val=head.val)
        temp, cur = head, keep
        while temp and temp.next:
            temp = temp.next
            node = ListNode(val=temp.val)
            cur.next = node
            cur = cur.next

        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp
            
        while prev:
            if keep.val != prev.val: return False
            keep, prev = keep.next, prev.next
        return True