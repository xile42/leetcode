class Solution:

    def minimumSum(self, n: int, k: int) -> int:

        ans = [1]
        for i in count(2):
            if 2 * i == k:
                ans.append(i)
                break
            if i + i - 1 == k:
                break
            if i >= k:
                break
            ans.append(i)

        cur = max(k, ans[-1] + 1)
        while len(ans) < n:
            ans.append(cur)
            cur += 1

        return sum(ans[:n])
