class Solution:

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def f(n):

            sn = str(n)

            return int("".join(map(str, [mapping[int(c)] for c in sn])))

        ns = [[f(v), i, v] for i, v in enumerate(nums)]
        ns.sort(key=lambda x: x[:2])

        return [v for _, _, v in ns]
