class Solution:

    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort()
        ns = [i[0] for i in items]
        mx = list()
        for i in range(len(items)):
            if not mx:
                mx.append(items[i][-1])
            else:
                mx.append(max(mx[-1], items[i][-1]))

        ans = list()
        for q in queries:
            i = bisect_right(ns, q)
            ans.append(0 if i == 0 else (mx[i - 1] if i < len(mx) else mx[-1]))

        return ans
