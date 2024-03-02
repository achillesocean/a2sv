class Solution:
    def trap(self, heights: List[int]) -> int:
        # at a "block", we can store amount of difference between min(maxleft so far!!stack!! and maxright) - block_height.
        n = len(heights) 
        if not heights: return 0
        maxLeft = [0] * n
        maxRight = [0] * n
        storage = 0
        #populate fist.
        for ind in range(1, n):
            maxLeft[ind] = max(maxLeft[ind - 1], heights[ind - 1])
            maxRight[n - 1 - ind] = max(maxRight[n - 1 - ind + 1], heights[n - 1 - ind + 1])
        for ind, num in enumerate(heights):
            storage += min(maxRight[ind], maxLeft[ind]) - num if min(maxRight[ind], maxLeft[ind]) - num > 0 else 0
        
        print(maxRight, maxLeft)
        return storage