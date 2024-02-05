class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #check then update record
        records = [-1] * (max(cards) + 1)
        n = len(cards)
        minlen = float("inf")
        for r in range(n):
            if records[cards[r]] != -1:
                minlen = min(minlen, r - records[cards[r]] + 1)
            records[cards[r]] = r

        return minlen if minlen != float("inf") else -1
