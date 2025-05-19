class Solution:

    def stringSequence(self, target: str) -> List[str]:

        ans = list()
        for idx, c in enumerate(target):
            this_bit = list()
            cur = "a"
            prefix = "" if not ans else ans[-1]
            while cur != c:
                this_bit.append(prefix + cur)
                cur = chr(ord(cur) + 1)
            this_bit.append(prefix + cur)
            ans += this_bit

        return ans
