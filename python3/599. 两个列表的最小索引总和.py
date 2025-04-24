class Solution:

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        d = defaultdict(int)
        d1 = {v: i for i, v in enumerate(list1)}
        d2 = {v: i for i, v in enumerate(list2)}

        results = list()
        for k in set(list1) & set(list2):
            d[k] += d1[k]
            d[k] += d2[k]

        if len(d) == 0:
            return results

        mn = min(d.values())
        for k, v in d.items():
            if v == mn:
                results.append(k)

        return results
