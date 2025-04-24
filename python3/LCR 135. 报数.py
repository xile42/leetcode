class Solution:

    def countNumbers(self, cnt: int) -> List[int]:

        return list(range(1, int("9" * cnt) + 1))
