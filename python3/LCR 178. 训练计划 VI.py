class Solution:

    def trainingPlan(self, actions: List[int]) -> int:

        c = Counter(actions)
        mn = min(c.values())
        for k in c:
            if c[k] == mn:
                return k
