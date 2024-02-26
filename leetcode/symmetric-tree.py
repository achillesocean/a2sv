# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, ans):
        #preorder
        if not root: 
            ans.append(None)
            return
        ans.append(root.val)
        self.helper(root.left, ans)
        self.helper(root.right, ans)
    def helper2(self, root, ans):
        if not root:
            ans.append(None)
            return
        ans.append(root.val)
        self.helper2(root.right, ans)
        self.helper2(root.left, ans)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #when you go left in one subtree, go right within the other
        #go left, go right, test
        ans_left = []
        self.helper(root.left, ans_left)
        ans_right = []
        self.helper2(root.right, ans_right)
        # print(ans_right)
        return False if ans_right != ans_left else True