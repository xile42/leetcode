class Solution:

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        xs = [[i[0], i[2]] for i in rectangles]
        ys = [[i[1], i[3]] for i in rectangles]

        # print("xs", xs)
        # print("ys", ys)
        def check(xs):

            xs = sorted(xs)
            # print("in check", xs)
            cur = xs[0]
            groups = list()
            for other in xs[1:]:
                # print("cur groups", groups)
                if len(groups) >= 3:
                    return True
                if cur[1] > other[0]:
                    # print("merge", cur, other)
                    cur = [cur[0], max(cur[1], other[1])]
                    continue
                else:
                    # print("split", cur, other)
                    groups.append(cur)
                    cur = other
                    continue

            return True if len(groups) >= 2 else False

        return check(xs) or check(ys)
