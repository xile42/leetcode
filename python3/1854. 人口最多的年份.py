class Solution:

    def maximumPopulation(self, logs: List[List[int]]) -> int:

        min_y = min(set(i[0] for i in logs))
        max_y = max(max(set(i[1] for i in logs)), max(set(i[1] for i in logs)))
        birth = defaultdict(int)
        death = defaultdict(int)
        for b, d in logs:
            birth[b] += 1
            death[d] += 1
        bs = list(accumulate([birth[y] for y in range(min_y, max_y + 1)]))
        ds = list(accumulate([death[y] for y in range(min_y, max_y + 1)]))
        live = [bs[y] - ds[y] for y in range(len(bs))]

        return min_y + live.index(max(live))
