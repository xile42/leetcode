class Solution:

    def totalNumbers(self, digits: List[int]) -> int:

        s = set()
        sd = [str(i) for i in digits]
        n = len(sd)
        for i in range(n):
            if sd[i] == "0":
                continue
            for j in range(n):
                for k in range(n):
                    if sd[k] not in {"0", "2", "4", "6", "8"}:
                        continue
                    if i != j and j != k and k != i:
                        s.add(sd[i] + sd[j] + sd[k])

        return len(s)