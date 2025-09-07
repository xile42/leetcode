class Solution:

    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        d = {v: i for i, v in enumerate(order)}
        ans = sorted(friends, key=lambda x: d[x])

        return ans
