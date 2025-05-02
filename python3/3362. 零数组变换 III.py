from bisect import bisect_left


class Solution:

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        if all(i == 0 for i in nums):
            return len(queries)

        diff = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            diff.append(nums[i] - nums[i - 1])
        diff.append(0)

        def update(l, r):

            nonlocal diff
            diff[l] -= 1
            diff[r + 1] += 1

        def fetch(v):

            results = list()
            idx = bisect_right(ls, v) - 1
            # print("in fetch, v:", v, "idx:", idx)
            while idx >= 0:
                l, r = queries[idx]
                if not vis[idx] and l <= v <= r:
                    results.append([idx, l, r])
                idx -= 1
            results = sorted(results, key=lambda x: x[2] - v, reverse=True)

            return results

        queries.sort()
        ls = [lr[0] for lr in queries]
        vis = [False for _ in range(len(queries))]
        # print("queries:", queries)
        # print("ls:", ls)
        # print("diff:", diff)
        cur = 0
        for diff_idx in range(len(diff) - 1):
            v = diff[diff_idx]
            cur += v
            # print("cur:", cur)
            if cur <= 0:
                continue
            candidates = fetch(diff_idx)
            # print("return candidates:", candidates)
            if len(candidates) < cur:
                return -1
            for idx, l, r in candidates[:cur]:
                vis[idx] = True
                update(l, r)
            cur = 0
            # print("update candidates:", candidates)
            # print("update diff:", diff)
            # print("update vis:", vis)
            # print("----------")

        return len(vis) - sum(vis)
