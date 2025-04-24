class Solution:

    def countLargestGroup(self, n: int) -> int:

        c = Counter()
        for i in range(1, n + 1):
            c[sum(map(int, str(i)))] += 1

        cc = Counter(c.values())

        return cc[max(c.values())]
