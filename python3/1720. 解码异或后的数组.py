class Solution:

    def decode(self, encoded: List[int], first: int) -> List[int]:

        ans = list()
        ans.append(first)
        for i in range(len(encoded)):
            ans.append(ans[-1] ^ encoded[i])

        return ans
