class Solution:

    def buildArray(self, target: List[int], n: int) -> List[str]:

        cur = list()
        result = list()

        for i in range(1, n+1):
            if i in target:
                result += ["Push"]
                cur += [i]
                if cur == target:
                    return result
            else:
                result += ["Push", "Pop"]
