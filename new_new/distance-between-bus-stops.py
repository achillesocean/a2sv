class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        #distance[i] = distance from stop i to stop i + 1
        #sum of distance from stop i to stop i + 1 == sum(distance[start:stop])
        if destination > start:
          return min(sum(distance[start:destination]), sum(distance[:start]) + sum(distance[destination:]))
        else:
          return min(sum(distance[start:]) + sum(distance[:destination]), sum(distance[destination:start]))