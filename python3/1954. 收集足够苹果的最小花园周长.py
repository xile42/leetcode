acc = [0, 12]
while acc[-1] < 10 ** 15:
    n = len(acc)
    acc.append(acc[-1] + (n + n * 2) * (n * 2 - n + 1) // 2 * 8 - (n * 2) * 4 - n * 4)


class Solution:

    def minimumPerimeter(self, neededApples: int) -> int:

        i = bisect_left(acc, neededApples)

        return i * 8
