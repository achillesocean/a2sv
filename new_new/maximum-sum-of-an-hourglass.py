class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        #you can't create an hour glass with the last two rows
        res = 0
        for row in range(len(grid) - 2):
            temp = 0
            for r in range(len(grid[row])):
                if r + 2 < len(grid[row]):
                    temp += (grid[row][r] + grid[row][r+1] + grid[row][r+2] + grid[row+1][r + 1] + grid[row+2][r] + grid[row+2][r+1] + grid[row+2][r+2])
                res = max(res, temp)
                temp = 0
        return res
                

        