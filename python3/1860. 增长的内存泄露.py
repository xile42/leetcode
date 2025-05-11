class Solution:

    def memLeak(self, memory1: int, memory2: int) -> List[int]:

        a, b = memory1, memory2
        for i in count(1):
            if a >= b:
                if a < i:
                    return [i, a, b]
                else:
                    a -= i
            else:
                if b < i:
                    return [i, a, b]
                else:
                    b -= i
