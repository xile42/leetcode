class Solution:

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # return sum(sorted(reduce(add, [[i[1]] * i[0] for i in boxTypes]))[-truckSize:])
        ans = 0
        bs = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        cur = truckSize
        idx = 0
        while cur != 0 and idx < len(bs):
            use = min(cur, bs[idx][0])
            ans += use * bs[idx][1]
            cur -= use
            idx += 1

        return ans
