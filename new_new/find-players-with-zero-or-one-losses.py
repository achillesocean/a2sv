class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = defaultdict(int)
        losers = defaultdict(int)
        for i in range(len(matches)):
            winners[matches[i][0]] += 1
            losers[matches[i][1]] += 1
        winners = [i for i in winners if losers[i] == 0]
        losers = [i for i in losers if losers[i] == 1]
        winners.sort()
        losers.sort()
        return [winners, losers]

        