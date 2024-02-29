class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        pack = deque()
        deck.sort()
        
        for i in range(len(deck) - 1, -1, -1):
            if not pack:
                pack.append(deck[i])
            else:
                temp = pack.pop()
                pack.appendleft(temp)
                pack.appendleft(deck[i])

        return pack