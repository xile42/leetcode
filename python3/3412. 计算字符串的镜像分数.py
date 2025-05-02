import string


class Solution:

    def calculateScore(self, s: str) -> int:

        d = {c: chr(25 - i + ord("a")) for i, c in enumerate(string.ascii_lowercase)}
        cnt = Counter()
        idxs = defaultdict(list)

        ans = 0
        for i, cur in enumerate(s):
            tar = d[cur]
            if cnt[tar] > 0:
                ans += i - idxs[tar][-1]
                cnt[tar] -= 1
                idxs[tar].pop(-1)
            else:
                cnt[cur] += 1
                idxs[cur].append(i)

        return ans
