# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ret = []
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        quot = length // k
        rem = length % k
        cur = head #to use just the one pointer
        for i in range(k):
            ret.append(cur)
            for j in range(quot - 1 + (1 if rem else 0)):
                if not cur: break
                cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            rem -= 1 if rem else 0
        return ret
            
