class Solution:

    def buttonWithLongestTime(self, events: List[List[int]]) -> int:

        ans = [[i, t] if idx == 0 else [i, t - events[idx - 1][1]]for idx, (i, t) in enumerate(events)]
        ans = sorted(ans, key=lambda x: x[1], reverse=True)
        v = ans[0][1]
        candidates = list()
        for i, t in ans:
            if t == v:
                candidates.append(i)
            else:
                break

        return min(candidates)