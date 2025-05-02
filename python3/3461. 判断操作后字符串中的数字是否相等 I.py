class Solution:
    def hasSameDigits(self, s: str) -> bool:

        cur = s
        while len(cur) != 2:
            this_ans = list()
            for a, b in pairwise(cur):
                this_ans.append(str((int(a) + int(b)) % 10))
            cur = "".join(this_ans)

        return len(set(cur)) == 1
