class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        cnt = 0
        ans = 0
        for c, ite in groupby(flowerbed):
            l = len(list(ite))
            if c == 1:
                cnt += l
                continue
            if cnt == 0 and cnt + l == len(flowerbed):
                return ceil(l / 2) >= n
            if cnt == 0 or cnt + l == len(flowerbed):
                ans += ceil((l - 1) / 2)
            else:
                ans += ceil((l - 2) / 2)
            cnt += l

        return ans >= n
