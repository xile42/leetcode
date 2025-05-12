class Solution:

    def smallestNumber(self, num: int) -> int:

        c = Counter(str(abs(num)))
        sk = list(sorted(c.keys()))

        if sk == ["0"]:
            return 0

        if "0" in sk:
            if num >= 0:
                ans = "".join([sk[i] * c[sk[i]] for i in range(1, len(sk))])
                ans = ans[0] + sk[0] * c[sk[0]] + ans[1:]
            else:
                ans = "".join([sk[i] * c[sk[i]] for i in range(len(sk) - 1, -1, -1)])
        else:
            if num >= 0:
                ans = "".join([sk[i] * c[sk[i]] for i in range(len(sk))])
            else:
                ans = "".join([sk[i] * c[sk[i]] for i in range(len(sk) - 1, -1, -1)])

        return int(ans) * (1 if num >= 0 else -1)
