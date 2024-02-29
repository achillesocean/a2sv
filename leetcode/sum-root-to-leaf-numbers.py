# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, cur, ans):
        # if not root: 
        #     if cur: 
        #         ans.append(cur)
        #         cur = cur[:len(cur)-1]
        #     return
        cur += str(root.val)
        if root.left: self.helper(root.left, cur, ans)
        if root.right: self.helper(root.right, cur, ans)
        #return up with one less from the end
        if not root.left and not root.right:
            ans.append(cur)
        cur = cur[:len(cur)-1]
        return
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #preorder=>concatenate itself. then go left.
        #if root.left is None: ans.append(cur)
        cur = ""
        ans = []
        self.helper(root, cur, ans)
        ret = 0
        for i in ans:
            if i != "":
                ret += int(i)
        return ret