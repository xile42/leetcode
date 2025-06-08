class Solution:

    def canMakeEqual(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        ns = copy.deepcopy(nums)
        tar = 1
        used = 0
        for i in range(n - 1):
            v = ns[i]
            if v != tar:
                if used >= k:
                    break
                else:
                    used += 1
                    ns[i + 1] *= -1
            else:
                continue
        else:
            if ns[n - 1] == tar:
                return True

        ns = copy.deepcopy(nums)
        tar = -1
        used = 0
        for i in range(n - 1):
            v = ns[i]
            if v != tar:
                if used >= k:
                    break
                else:
                    used += 1
                    ns[i + 1] *= -1
            else:
                continue
        else:
            if ns[n - 1] == tar:
                return True

        return False
