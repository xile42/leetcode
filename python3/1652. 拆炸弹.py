class Solution:

    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)
        ns = code + code + code
        ans = list()
        for i in range(n, n * 2):
            if k > 0:
                ans.append(sum(ns[i + 1:i + 1 + k]))
            elif k < 0:
                ans.append(sum(ns[i - abs(k):i]))
            else:
                ans.append(0)

        return ans
