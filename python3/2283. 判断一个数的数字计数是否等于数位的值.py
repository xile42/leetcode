class Solution:

    def digitCount(self, num: str) -> bool:

        c = Counter(map(int, num))

        return all(int(num[i]) == c[i] for i in range(len(num)))
