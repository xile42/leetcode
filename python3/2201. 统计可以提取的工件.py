class Solution:

    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:

        valid = dict()
        cnt = Counter()
        for _id, (x, y, xx, yy) in enumerate(artifacts):
            for i in range(x, xx + 1):
                for j in range(y, yy + 1):
                    cnt[_id] += 1
                    valid[(i, j)] = _id

        ans = 0
        for x, y in dig:
            if (x, y) in valid:
                cnt[valid[(x, y)]] -= 1
                if cnt[valid[(x, y)]] == 0:
                    ans += 1

        return ans
