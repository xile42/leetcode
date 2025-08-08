class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        ps = [[pos, spd] for pos, spd in zip(position, speed)]
        ps.sort()

        cur = -inf
        ans = len(ps)
        for i in range(len(ps) - 1, -1, -1):
            pos, spd = ps[i]
            time = (target - pos) / spd
            if time <= cur:
                ans -= 1
            else:
                cur = time

        return ans
