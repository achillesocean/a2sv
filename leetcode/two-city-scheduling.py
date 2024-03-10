class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #a greedy algo solution pattern:think in terms of profit, especially when cost/loss exists.
        #...think in such two player/two choice scenarios how you could choose the one choice at all times, then the other
        #choice just the same, and try to construct some relation between the two choices.
        cost = 0
        storage = []
        for ind, val in enumerate(costs):
            storage.append([ind, val[1] - val[0]])

        storage.sort(key=lambda x:x[1])

        i = 0
        while i < len(costs):
            if i < len(costs) // 2:
                #send to b
                cost += costs[storage[i][0]][1]
            else:
                #send to a
                cost += costs[storage[i][0]][0]

            i += 1

        return cost