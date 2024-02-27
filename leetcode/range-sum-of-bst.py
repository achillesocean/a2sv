# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Preorder traversal 
        ans = 0
        def helper(node):
            nonlocal ans
            if not node: return
            ans += node.val if node.val <= high and node.val >= low else 0
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ans