class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        #go from the last column to the left. test for each row
        curcol = cols - 2
        row = 0
        for row in range(len(matrix)):
            while curcol >= 0:
                if row + 1 < rows and curcol + 1 < cols:
                    if matrix[row][curcol] != matrix[row + 1][curcol + 1]:
                        return False
                curcol -= 1
            
            curcol = cols - 2
        
        return True

        #1 2 3 4
        #5 2 1 3
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        