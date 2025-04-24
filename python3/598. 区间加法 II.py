class Solution:

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        return m * n if not ops else min([i[0] for i in ops]) * min([i[1] for i in ops])
