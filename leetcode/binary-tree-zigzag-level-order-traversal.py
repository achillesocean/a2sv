# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        ans = []
        # Each level's nodes in a list
        # Recording all the nodes on the same level
        # and another recording of the new level of nodes.
        def rightLeft(cur, prev):# LIFO for the prev
        # copy over the cur to prev? if so, then LIFO for cur as well.
            while prev:
                root = prev.pop()
                if root.right:
                    cur.append(root.right)
                if root.left:
                    cur.append(root.left)
            if cur:
                prev = cur[:]
            else: return
            ans.append([node.val for node in cur])
        # copy cur over to prev, empty cur, copy it over to ans as well.
            leftRight([], prev)
        
        def leftRight(cur, prev):
            while prev:
                root = prev.pop()
                if root.left:
                    cur.append(root.left)
                if root.right:
                    cur.append(root.right)
            if cur:
                prev = cur[:]
            else: return
            ans.append([node.val for node in cur])
            rightLeft([], prev)
        leftRight([root], [])
        return ans