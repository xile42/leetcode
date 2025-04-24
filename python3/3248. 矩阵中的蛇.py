class Solution:

    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        ho = sum(1 if c == "RIGHT" else -1 for c in commands if c in {"RIGHT", "LEFT"})
        vo = sum(1 if c == "DOWN" else -1 for c in commands if c in {"UP", "DOWN"})

        return vo * n + ho
