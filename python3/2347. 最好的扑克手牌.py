class Solution:

    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        if len(set(suits)) == 1:
            return "Flush"

        c = Counter(ranks)
        v = max(c.values())
        if v >= 3:
            return "Three of a Kind"

        if v >= 2:
            return "Pair"

        return "High Card"
