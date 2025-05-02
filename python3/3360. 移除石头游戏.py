class Solution:

    def canAliceWin(self, n: int) -> bool:

        turn = 0
        cur = 10
        while True:
            if n < cur:
                if turn == 0:
                    return False
                return True
            n -= cur
            cur -= 1
            turn = 1 - turn