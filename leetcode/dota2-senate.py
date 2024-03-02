class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senates = list(senate)
        senate_q = deque()
        for s in senates:
            if not senate_q:
                senate_q.append(s)
            else:
                if s == senate_q[0]:
                    senate_q.append(s)
                else:
                    senates.append(senate_q.popleft())

        if senate_q and senate_q[0] == "R": return "Radiant"
        if senate_q and senate_q[0] == "D": return "Dire"