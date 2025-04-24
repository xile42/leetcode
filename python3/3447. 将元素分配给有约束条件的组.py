class Solution:

    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:

        mx = max(groups)
        d = defaultdict(lambda: -1)
        for i, n in enumerate(elements):
            cur = n
            if d[cur] != -1:
                continue
            while cur <= mx:
                if d[cur] == -1:
                    d[cur] = i
                cur += n

        return [d[i] for i in groups]
