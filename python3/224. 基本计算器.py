class Solution:

    def calculate(self, s: str) -> int:

        n = len(s)
        sts = list()
        sts.append(list())

        def get_next(i):

            while i < n and s[i] == " ":
                i += 1

            if i >= n:
                return i, None

            c = s[i]
            if c == "+":
                return i + 1, "+"
            elif c == "-":
                return i + 1, "-"
            elif c == "(":
                return i + 1, "("
            elif c == ")":
                return i + 1, ")"
            else:
                cur = c
                while i + 1 < n and s[i + 1].isdigit():
                    i += 1
                    cur += s[i]
                return i + 1, int(cur)

        sts.append(list())
        i = 0
        while i < n:
            ii, cur = get_next(i)
            if cur is None:
                break
            if cur == "+":
                sts[-1].append(cur)
            elif cur == "-":
                sts[-1].append(cur)
            elif cur == "(":
                sts.append(list())
            elif cur == ")":
                value = sts[-1][-1]
                sts.pop(-1)
                if len(sts[-1]) == 0:
                    sts[-1].append(value)
                elif sts[-1][-1] == "+":
                    sts[-1].pop(-1)
                    other = sts[-1].pop(-1)
                    sts[-1].append(other + value)
                elif sts[-1][-1] == "-":
                    if len(sts[-1]) == 1:
                        sts[-1].append(-value)
                    else:
                        sts[-1].pop(-1)
                        other = sts[-1].pop(-1)
                        sts[-1].append(other - value)
            else:
                if len(sts[-1]) == 0:
                    sts[-1].append(cur)
                elif sts[-1][-1] == "+":
                    sts[-1].pop(-1)
                    other = sts[-1].pop(-1)
                    sts[-1].append(other + cur)
                elif sts[-1][-1] == "-":
                    if len(sts[-1]) == 1:
                        sts[-1].append(-cur)
                    else:
                        sts[-1].pop(-1)
                        other = sts[-1].pop(-1)
                        sts[-1].append(other - cur)

            i = ii

        return sts[-1][-1]
