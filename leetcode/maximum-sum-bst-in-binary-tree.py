# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        #checking and validating the BST properties and computes the sum of the subtree keys until the maximum sum of any BST subtree within the overall tree is identified.

        ans = 0
        #return boundaries are for parent node validations.

        def dfs(node):
            #do we validate after left and right returns?
            if not node:
                return (1, math.inf, -math.inf, 0)# T/F, min, max, sum
            
            left_check, lmin, lmax, lsum = dfs(node.left)
            right_check, rmin, rmax, rsum = dfs(node.right)
            
            if left_check and right_check:
                if node.val < rmin and node.val > lmax:
                    sub_sum = node.val + lsum + rsum
                    nonlocal ans
                    ans = max(ans, sub_sum)
                    return (1, min(lmin, node.val), max(rmax, node.val), sub_sum)
            #not a valid subtree otherwise
            return (0, 0, 0, 0)

        dfs(root)
        return ans