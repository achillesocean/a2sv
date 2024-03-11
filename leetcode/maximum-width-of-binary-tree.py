# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        new binary tree pattern!!
        Breadth-First Search (BFS) is a suitable approach since we need to explore levels.
        During BFS, instead of storing the node values, we can store the indices assigned to each node in the level.
        The index of the root node in a level is usually set to 1.
        In each level, track the index of the first non-null node (leftmost) and the last non-null node (rightmost).
        The width of the current level is simply rightmost - leftmost + 1.
        Keep track of the maximum width encountered so far and update it if needed.
        '''

        width = 0
        q = deque([[root, 1, 0]]) #node, index, level
        #when a new level is encountered, register the first index. use prevIndex for that.
        prevLevel, prevIndex = 0, 1
        #prevIndex = 1 because every novel level's first entry should have length of 1. to make this hold for the root, prevIndex has to be = 1

        while q:
            node, index, level = q.popleft()

            if level > prevLevel:
                prevIndex = index
                prevLevel = level

            width = max(width, index - prevIndex + 1)

            if node.left:
                q.append([node.left, 2 * index, level + 1])
            if node.right:
                q.append([node.right, 2 * index + 1, level + 1])
                
        return width
