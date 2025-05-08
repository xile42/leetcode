class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        ans = list()
        for i in range(left, right + 1):
            si = str(i)
            if "0" in si:
                continue
            success = True
            for c in si:
                if i % int(c) != 0:
                    success = False
                    break
            if success:
                ans.append(i)

        return ans