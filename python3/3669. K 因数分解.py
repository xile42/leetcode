class Solution:

    def minDifference(self, n: int, k: int) -> List[int]:

        ans = inf
        ans_path = None

        def dfs(cur, k, low, path):

            nonlocal ans, ans_path
            if k == 1:
                if cur < low:
                    return
                full_path = path + [cur]
                diff = max(full_path) - min(full_path)
                if diff < ans:
                    ans = diff
                    ans_path = full_path
                return

            limit = 1
            while True:
                next_val = limit + 1
                if next_val ** k > cur:
                    break
                limit = next_val

            factors = set()
            i = 1
            while i * i <= cur:
                if cur % i == 0:
                    if low <= i <= limit:
                        factors.add(i)
                    j = cur // i
                    if low <= j <= limit:
                        factors.add(j)
                i += 1

            for factor in factors:
                dfs(cur // factor, k - 1, factor, path + [factor])

        dfs(n, k, 1, list())

        return ans_path
