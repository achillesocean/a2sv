# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, counter, max_count):
        if not root:
            return max_count  # Return the current max_count

        counter[root.val] += 1
        max_count = max(max_count, counter[root.val])

        max_count = self.helper(root.left, counter, max_count)  # Update max_count from children
        max_count = self.helper(root.right, counter, max_count)

        return max_count  # Return the updated max_count

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = defaultdict(int)
        max_count = self.helper(root, counter, 0)  # Initiate max_count calculation

        ret = []
        for key in counter:
            if counter[key] == max_count:
                ret.append(key)

        return ret  # Return the list of modes