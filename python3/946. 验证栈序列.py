class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        if not len(pushed) == len(popped):
            return False

        s = []
        idx = 0

        for c in pushed:

            if c == popped[idx]:
                idx += 1
            else:
                s.append(c)

            while s and idx < len(popped) and s[-1] == popped[idx]:
                s.pop(-1)
                idx += 1

        if len(s) == 0 and idx == len(popped):
            return True

        return False
