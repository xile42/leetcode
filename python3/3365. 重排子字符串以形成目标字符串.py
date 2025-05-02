class Solution:

    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:

        l = len(s) // k
        parts1 = [s[i * l:(i + 1) * l] for i in range(k)]
        parts2 = [t[i * l:(i + 1) * l] for i in range(k)]

        c = Counter(parts1)
        for part in parts2:
            if part in c and c[part] > 0:
                c[part] -= 1
            else:
                return False

        return True

        # l = len(s) // k
        # parts1 = [Counter(s[i * l:(i + 1) * l]) for i in range(k)]
        # parts2 = [Counter(t[i * l:(i + 1) * l]) for i in range(k)]

        # cs1 = list()
        # for c in parts1:
        #     t = list()
        #     for key, value in c.items():
        #         t.append("{}{}".format(key, value))
        #     cs1.append("".join(sorted(t)))
        # cs1.sort()
        #
        # cs2 = list()
        # for c in parts2:
        #     t = list()
        #     for key, value in c.items():
        #         t.append("{}{}".format(key, value))
        #     cs2.append("".join(sorted(t)))
        # cs2.sort()

        # print(cs1)
        # print(cs2)
        # return cs1 == cs2
