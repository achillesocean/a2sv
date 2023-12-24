class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        cols = len(mat[0])
        rows = len(mat)
        r = c = 0
        going_up = True

        while len(output) != cols * rows:
            #go up first
            #then go down from the 0th row
            if going_up:
                while r >= 0 and c < cols:
                    output.append(mat[r][c])
                    r -= 1
                    c += 1
                if c == cols:
                    c -= 1
                    r += 2
                else:
                    r += 1
                going_up = False
            else:
                while r < rows and c >= 0:
                    output.append(mat[r][c])
                    c -= 1
                    r += 1
                if r == rows:
                    r -= 1
                    c += 2
                else:
                    c += 1
                going_up = True
        
        return output

        '''
        00 going up
        01 going down
        10
        20 going up
        11
        02
        12 going down
        21 
        22 going up. 
        going up means decreasing row, and increasing column
        going down means increasing row and decreasing column
        '''