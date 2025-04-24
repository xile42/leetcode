class Solution:

    def wateringPlants(self, plants: List[int], capacity: int) -> int:

        ans = 0
        cur = capacity

        for i, need in enumerate(plants):
            if cur >= need:
                cur -= need
                ans += 1
            else:
                cur = capacity - need
                ans += 2 * (i + 1) - 1

        return ans
        