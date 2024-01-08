class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = (len(piles) * 2) // 3
        coins = 0
        piles.sort(reverse=True)
        for i in range(1, n, 2):
            coins += piles[i]

        return coins


        