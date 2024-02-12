# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        values = set()
        previous = None
        while current:
            if current.val in values:
                previous.next = current.next
                current = current.next
            else:
                values.add(current.val)
                previous = current
                current = current.next
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        