class Solution:

    result = None

    def search(self, candidates, chance, current):

        if chance == 0:
            self.result.append(current)
            return

        for idx, num in enumerate(candidates):
            if len(candidates) - idx < chance:
                break
            self.search(candidates[idx+1:], chance-1, current+[num])

    def combine(self, n: int, k: int) -> List[List[int]]:

        self.result = list()
        self.search(list(range(1, n+1)), k, list())

        return self.result
