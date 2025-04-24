class Solution:

    def canThreePartsEqualSum(self, arr: List[int]) -> bool:

        acc = list(accumulate(arr))
        if abs(acc[-1]) % 3 != 0:
            return False
        tar = abs(acc[-1]) // 3 * (-1 if acc[-1] < 0 else 1)

        cur = 0
        cnt = 0
        for v in acc:
            if v - cur == tar:
                cnt += 1
                cur += tar

        return cnt >= 3
