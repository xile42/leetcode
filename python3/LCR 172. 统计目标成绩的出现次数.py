class Solution:

    def countTarget(self, scores: List[int], target: int) -> int:

        return Counter(scores)[target]
