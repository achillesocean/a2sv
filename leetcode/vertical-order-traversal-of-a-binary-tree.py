# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        def helper(node, row, col):
            if not node: return
            nodes.append((row, col, node.val))
            helper(node.left, row + 1, col - 1)
            helper(node.right, row + 1, col + 1)

        helper(root, 0, 0)

        nodes.sort(key=lambda x: (x[1], x[0], x[2]))
        
        ans = []

        prev = -math.inf

        for node in nodes:
            if node[1] != prev:
                ans.append([])
            ans[-1].append(node[2])
            prev = node[1]

        return ans