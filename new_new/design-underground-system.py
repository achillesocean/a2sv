class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.totalTime = defaultdict(list)

    def checkIn(self, id: int, startStation: str, t: int) -> None:
        self.checkin[id] = [startStation, t]

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        self.totalTime[(self.checkin[id][0], endStation)] += [t - self.checkin[id][1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.totalTime[(startStation, endStation)]) / len(self.totalTime[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)