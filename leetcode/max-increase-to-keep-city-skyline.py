class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = 0
        west, south = [], [0] * len(grid)
        for r in range(len(grid)):
            row_max = -1
            for c in range(len(grid)):
                row_max = max(row_max, grid[r][c])
                south[c] = max(south[c], grid[r][c])
            west.append(row_max)
            
        for r in range(len(grid)):
            for c in range(len(grid)):
                ans += min(west[r], south[c]) - grid[r][c]
        return ans
            