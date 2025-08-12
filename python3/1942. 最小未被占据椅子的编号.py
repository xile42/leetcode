class Solution:

    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        ns = list()
        for i, (s, e) in enumerate(times):
            ns.append([s, 0, i])
            ns.append([e, 1, i])
        ns.sort(key=lambda x: [x[0], -x[1]])

        n = len(times)
        d = dict()
        h = list(range(n))
        for t, tp, i in ns:
            if tp == 0:
                _id = heappop(h)
                d[i] = _id
                if i == targetFriend:
                    return _id
            else:
                _id = d[i]
                heappush(h, _id)
