class Solution:

    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        xs = list()
        ys = set()
        cur = 1
        while cur < bound:
            xs.append(cur)
            cur *= x
            if x == 1:
                break
        cur = 1
        while cur < bound:
            ys.add(cur)
            cur *= y
            if y == 1:
                break

        def check(tar):

            for v in xs:
                if v > tar:
                    return False
                if tar - v in ys:
                    return True

            return False

        ans = list()
        for i in range(0, bound + 1):
            if check(i):
                ans.append(i)

        return ans
