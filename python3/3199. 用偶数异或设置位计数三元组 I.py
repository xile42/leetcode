class Solution:

    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        ans = 0
        for i in a:
            for j in b:
                for k in c:
                    n = i ^ j ^ k
                    if not n.bit_count() & 1:
                        ans += 1

        return ans
