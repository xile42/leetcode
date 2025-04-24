class Solution:

    def kthCharacter(self, k: int, operations: List[int]) -> str:

        ans = 0
        n = min(len(operations), k.bit_length())
        for i in range(n-1, -1, -1):
            m = (1 << i)
            if k > m:
                ans += operations[i]
                k -= m

        return ascii_lowercase[ans % 26]
