class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sq = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in rows[r]: return False
                    if board[r][c] in cols[c]: return False
                    if board[r][c] in sq[(r//3, c//3)]: return False
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    sq[(r//3, c//3)].add(board[r][c])

        return True
        