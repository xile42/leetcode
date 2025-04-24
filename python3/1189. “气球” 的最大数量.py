class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:

        need = {
            "b": 1,
            "a": 1,
            "l": 2,
            "o": 2,
            "n": 1,
        }
        c = Counter(text)
        times = list()
        for k, v in need.items():
            times.append(c[k] // v)

        return min(times)
