class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        n = len(baskets)
        vis = [False] * n
        ans = 0
        for v in fruits:
            success = False
            for i, b in enumerate(baskets):
                if not vis[i] and b >= v:
                    vis[i] = True
                    success = True
                    break
            if not success:
                ans += 1

        return ans
