class Solution:

    def buddyStrings(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False
        
        a, b = [], []
        for i, j in zip(s, goal):
            if i != j:
                a.append(i)
                b.append(j)

        return (len(a) == 0 and max(Counter(s).values()) > 1) or (len(a) == len(b) == 2 and Counter(a) == Counter(b))
