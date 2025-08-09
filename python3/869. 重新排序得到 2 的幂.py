class Solution:

    def reorderedPowerOf2(self, n: int) -> bool:

        sn = str(n)
        for comb in permutations(list(sn)):
            if comb[0] == "0":
                continue
            cur = int("".join(comb))
            if cur.bit_count() == 1:
                return True

        return False
