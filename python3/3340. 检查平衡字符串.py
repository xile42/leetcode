class Solution:

    def isBalanced(self, num: str) -> bool:

        a = sum([int(num[i]) for i in range(len(num)) if i & 1])
        b = sum([int(num[i]) for i in range(len(num)) if not i & 1])

        return a == b

