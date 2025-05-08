class Solution:

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        n = len(hand)
        if n % groupSize != 0:
            return False

        c = Counter(hand)

        for _ in range(n // groupSize):
            start = min(c.keys())
            ns = list(range(start, start + groupSize))
            for k in ns:
                if c[k] <= 0:
                    return False
                c[k] -= 1
                if c[k] == 0:
                    del c[k]

        return True
