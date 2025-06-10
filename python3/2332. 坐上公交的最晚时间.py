class Solution:

    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:

        buses.sort()
        passengers.sort()
        sp = set(passengers)

        i = j = 0
        cur = capacity
        last_full = False
        while i < len(buses) and j < len(passengers):
            bt = buses[i]
            pt = passengers[j]
            if cur == 0:
                last_full = True
                cur = capacity
                i += 1
            elif bt < pt:
                last_full = False
                cur = capacity
                i += 1
            else:
                j += 1
                cur -= 1
                if cur == 0:
                    last_full = True

        if i < len(buses) - 1:
            last_full = False

        if not last_full:
            t = buses[-1]
            while t in sp:
                t -= 1
            return t

        t = passengers[j - 1]
        while t in sp:
            t -= 1

        return t
