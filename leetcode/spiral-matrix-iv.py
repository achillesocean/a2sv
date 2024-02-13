# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        l, r = 0, n - 1
        u, d = 0, m - 1
        while r >= l and d >= u:
            #c = l then increment for a given r = u ##to right traversal
            for c in range(l, r + 1):
                if head:
                    matrix[u][c] = head.val 
                    head = head.next
            u += 1
            for c in range(u, d + 1):
                if head:
                    matrix[c][r] = head.val
                    head = head.next
            r -= 1
            for c in range(r, l - 1, -1):
                if head:
                    matrix[d][c] = head.val
                    head = head.next
            d -= 1
            for c in range(d, u - 1, -1):
                if head:
                    matrix[c][l] = head.val
                    head = head.next
            l += 1
        return matrix
        