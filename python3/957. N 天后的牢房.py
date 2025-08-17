class Solution:

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:

        queue = list()

        def f(cells):

            ans = [0] * len(cells)
            for i in range(1, len(cells) - 1):
                ans[i] = int(cells[i - 1] == cells[i + 1])

            return ans

        while True:
            cur = tuple(f(cells))
            if queue and cur == queue[0]:
                break
            queue.append(cur)
            cells = cur

        return list(queue[(n - 1) % len(queue)])
