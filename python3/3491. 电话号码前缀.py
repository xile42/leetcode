class Solution:

    def phonePrefix(self, numbers: List[str]) -> bool:

        ss = sorted(numbers)
        for i, s in enumerate(ss):
            if i < len(ss) - 1 and ss[i + 1][:len(s)] == s:
                return False

        return True
