class Solution:

    def maximumValue(self, strs: List[str]) -> int:

        return max(int(w) if w.isdigit() else len(w) for w in strs)
