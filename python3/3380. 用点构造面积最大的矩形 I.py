class Solution:

    def maxRectangleArea(self, points: List[List[int]]) -> int:

        cx = sorted(Counter([xy[0] for xy in points]).items())
        cy = sorted(Counter([xy[1] for xy in points]).items())
        xy_set = set(map(tuple, points))
        valid_x = list()
        valid_y = list()

        for x in cx:
            if x[1] > 1:
                valid_x.append(x[0])
        for y in cy:
            if y[1] > 1:
                valid_y.append(y[0])

        ans = -1
        for i in range(len(valid_x)):
            xs = valid_x[i]
            for j in range(i + 1, len(valid_x)):
                xe = valid_x[j]
                for k in range(len(valid_y)):
                    ys = valid_y[k]
                    for l in range(k + 1, len(valid_y)):
                        ye = valid_y[l]
                        a = (xs, ys)
                        b = (xs, ye)
                        c = (xe, ys)
                        d = (xe, ye)
                        abcd = set([a, b, c, d])
                        if all(i in xy_set for i in abcd):
                            valid = True
                            for x, y in xy_set:
                                if (x, y) not in abcd and xs <= x <= xe and ys <= y <= ye:
                                    valid = False
                                    break
                            if valid:
                                ans = max(ans, (xe - xs) * (ye - ys))

        return ans

        # cx = sorted(Counter([xy[0] for xy in points]).items())
        # cy = sorted(Counter([xy[1] for xy in points]).items())
        # xy_set = set(map(tuple, points))
        # x_pairs = list()
        # y_pairs = list()
        # for x1, x2 in pairwise(cx):
        #     if x1[1] > 1 and x2[1] > 1:
        #         x_pairs.append([x1[0], x2[0]])
        # for y1, y2 in pairwise(cy):
        #     if y1[1] > 1 and y2[1] > 1:
        #         y_pairs.append([y1[0], y2[0]])
        # ans = -1
        # for xs, xe in x_pairs:
        #     for ys, ye in y_pairs:
        #         a = (xs, ys)
        #         b = (xs, ye)
        #         c = (xe, ys)
        #         d = (xe, ye)
        #         if all(i in xy_set for i in [a, b, c, d]):
        #             ans = max(ans, (xe - xs) * (ye - ys))
        #
        # return ans