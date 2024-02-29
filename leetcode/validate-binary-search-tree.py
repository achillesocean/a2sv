# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left, right):
            # Test the current node you're at.
            if not node: return True
            if node.val <= left or node.val >= right: return False

            # Redefine left, and right limits.
            # when you go left, you wanna inherit the parent's left limit.
            # when you go right, redefine the left limit.
            # when you go left, redefine the right limit.
            return helper(node.left, left, node.val) and helper(node.right, node.val, right)
        
        return helper(root, float("-inf"), float("inf"))