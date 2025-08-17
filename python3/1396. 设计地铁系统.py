class UndergroundSystem:

    def __init__(self):

        self.in_time = dict()
        self.records = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.in_time[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        in_station, in_time = self.in_time[id]
        out_station, out_time = stationName, t
        self.records[(in_station, out_station)].append(out_time - in_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        return sum(self.records[(startStation, endStation)]) / len(self.records[(startStation, endStation)])

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)