class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:

        devices = [sum(map(int, row)) for row in bank if sum(map(int, row)) != 0]

        if len(devices) <= 1:
            return 0

        return sum([devices[idx] * devices[idx+1] for idx in range(len(devices)-1)])
