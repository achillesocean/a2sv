# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #I can do preorder traversal
        if root and root.val == val: return root
        if not root: return
        if val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
        #return None