# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        tmp = []
        cur = head
        while cur:
            tmp.append(cur.val)
            cur = cur.next
        num = 0
        for i in range(len(tmp)):
            num += tmp[i] * (2 ** (len(tmp) - 1 - i))
        return num
        