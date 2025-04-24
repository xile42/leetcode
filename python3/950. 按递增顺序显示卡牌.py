class Solution:

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        n = len(deck)
        deck = sorted(deck)
        ns = list(range(n))
        ans = [0] * n

        cur = 0
        while ns:
            i = ns.pop(0)
            ans[i] = deck[cur]
            cur += 1
            if not ns:
                break
            j = ns.pop(0)
            ns.append(j)

        return ans
