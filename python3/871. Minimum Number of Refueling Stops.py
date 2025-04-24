class Solution:

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        count = 0
        stations.append([target, 0])
        current_fuel = startFuel
        fuels = list()

        for idx, (station, fuel) in enumerate(stations):

            while len(fuels) and current_fuel < station:
                current_fuel -= heappop(fuels)
                count += 1

            if current_fuel < station:
                return -1

            heappush(fuels, -fuel)

        return count
