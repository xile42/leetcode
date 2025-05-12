class Solution:

    def minMoves(self, target: int, maxDoubles: int) -> int:

        cur = target
        ans = 0
        while cur != 1 and maxDoubles:
            if cur & 1:
                cur -= 1
                ans += 1
            cur //= 2
            ans += 1
            maxDoubles -= 1
        ans += cur - 1

        return ans
