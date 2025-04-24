class Solution:

    def largestGoodInteger(self, num: str) -> str:

        ns = [num[i-2:i+1] for i in range(2, len(num)) if len(set(num[i-2:i+1])) == 1]

        return str() if len(ns) == 0 else max(ns)
