class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range(len(matrix[0])):
            cur = []
            for j in matrix:
                cur.append(j[i])

            output.append(cur)
        
        return output