class Solution:

    def addRungs(self, rungs: List[int], dist: int) -> int:

        return sum(floor((rungs[i] - rungs[i - 1] - 1) / dist) for i in range(1, len(rungs))) + (rungs[0] - 1) // dist
