class Solution:

    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:

        ans = sum(reward2)
        ns = sorted([reward1[i] - reward2[i] for i in range(len(reward1))])
        if k:
            ans += sum(ns[-k:])

        return ans
