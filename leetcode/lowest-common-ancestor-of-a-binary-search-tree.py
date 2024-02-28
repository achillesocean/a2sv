# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #1 if one is bigger than the root, and the other is smaller, or viceversa, 
        #it means that they are on either side of the root.
        def helper(node):
            if node.val == p.val or node.val == q.val:
                return node
            if node.val > p.val and node.val < q.val:
                return node
            elif node.val < p.val and node.val > q.val:
                return node
            # Go left
            if node.val > p.val and node.val > q.val:
                return helper(node.left)
            # Go right
            elif node.val < p.val and node.val < q.val:
                return helper(node.right)
        
        return helper(root)