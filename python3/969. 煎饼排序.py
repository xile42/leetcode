class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:

        target = sorted(arr)
        d = {v: k for k, v in enumerate(arr)}
        ans = list()
        for tar in range(len(target) - 1, -1, -1):
            v = target[tar]
            i = d[v]
            if i == tar:
                continue
            ans += [i + 1, tar + 1]
            for key in d:
                value = d[key]
                if value <= i:
                    d[key] = i - value
            for key in d:
                value = d[key]
                if value <= tar:
                    d[key] = tar - value

        return ans
