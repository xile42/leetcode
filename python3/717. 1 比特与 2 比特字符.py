class Solution:

    def isOneBitCharacter(self, bits: List[int]) -> bool:

        ans = list()

        def f(ns, path):

            nonlocal ans
            if len(ns) == 0:
                ans.append(path)
                return

            if len(ns) == 1:
                if ns[0] != 0:
                    return
                f(ns[1:], path + [[ns[0]]])

            else:
                if not ((ns[0] == 0) or (ns[:2] == [1, 0] or ns[:2] == [1, 1])):
                    return
                if ns[0] == 0:
                    f(ns[1:], path + [[ns[0]]])
                if ns[:2] == [1, 0] or ns[:2] == [1, 1]:
                    f(ns[2:], path + [ns[:2]])

        f(bits, list())

        for path in ans:
            if len(path[-1]) > 1:
                return False

        return True
