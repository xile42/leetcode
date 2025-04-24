class Solution:

    def losingPlayer(self, x: int, y: int) -> str:

        a, b = x, y // 4
        c = min(a, b)

        return "Bob" if not c & 1 else "Alice"
