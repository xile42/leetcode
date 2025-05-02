class Solution:

    def getLargestOutlier(self, nums: List[int]) -> int:

        set_n = set(nums)
        c = Counter(nums)
        sn = sorted(set_n, reverse=True)
        s = sum(nums)

        for n in sn:
            left = s - n
            tar = left // 2
            if n == tar and c[n] <= 1:
                continue
            if left & 1 == 0 and tar in set_n:
                return n
