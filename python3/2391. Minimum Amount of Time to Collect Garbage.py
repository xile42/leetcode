class Solution:

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        from collections import defaultdict, Counter

        prefix_sum = list()
        count_map = defaultdict(int)
        last_map = defaultdict(lambda: -1)

        base_num = 0
        prefix_sum.append(base_num)
        for idx in range(len(travel)):
            base_num += travel[idx]
            prefix_sum.append(base_num)

        for idx, garbage_i in enumerate(garbage):
            counter = Counter(garbage_i)
            for k, v in counter.items():
                count_map[k] += v
                last_map[k] = idx

        result = 0
        for k in ["M", "P", "G"]:
            if count_map[k] == 0:
                continue
            result += count_map[k]
            result += prefix_sum[last_map[k]]

        return result
