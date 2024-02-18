class Solution:
    def minMoves(self, target: int, dbl: int) -> int:
        count = 0
        for _ in range(dbl):
            if target == 1: return count
            if target % 2 != 0:
                count += 1
            target //= 2
            count += 1
            if target == 1: return count
        return count + target - 1