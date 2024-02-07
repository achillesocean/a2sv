class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows, cols = len(self.matrix), len(self.matrix[0])
        for r in range(rows):
            acc = 0
            for c in range(cols):
                acc += self.matrix[r][c]
                self.matrix[r][c] = acc
        for c in range(cols):
            acc = 0
            for r in range(rows):
                acc += self.matrix[r][c]
                self.matrix[r][c] = acc

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sub1, sub2, add1 = 0, 0, 0
        if row1 - 1 >= 0:
            sub1 = self.matrix[row1 - 1][col2]
        if col1 - 1 >= 0:
            sub2 = self.matrix[row2][col1 - 1]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            add1 = self.matrix[row1 - 1][col1-1]

        ret = self.matrix[row2][col2] - sub1 - sub2 + add1
        return ret

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)