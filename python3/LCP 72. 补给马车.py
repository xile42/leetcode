class Solution:

    def supplyWagon(self, supplies: List[int]) -> List[int]:

        n = len(supplies) // 2
        while len(supplies) > n:
            idx = 1
            for i in range(1, len(supplies)):
                if supplies[i] + supplies[i - 1] < supplies[idx] + supplies[idx - 1]:
                    idx = i
            supplies[idx - 1] += supplies[idx]
            supplies.pop(idx)

        return supplies
