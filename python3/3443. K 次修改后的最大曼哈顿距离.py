class Solution:

    def maxDistance(self, s: str, k: int) -> int:

        xd = {"N": 0, "S": 0, "W": -1, "E": 1}
        yd = {"N": 1, "S": -1, "W": 0, "E": 0}
        od = {"W": "E", "E": "W", "S": "N", "N": "S"}
        ans = -inf
        tar_xs = ["W", "E"]
        tar_ys = ["S", "N"]
        for tar_x in tar_xs:
            for tar_y in tar_ys:
                x = 0
                y = 0
                chance = k
                for i, _ in enumerate(s):
                    c = s[i]
                    if chance and (c == tar_x or c == tar_y):
                        c = od[c]
                        chance -= 1
                    x += xd[c]
                    y += yd[c]
                    d = abs(x) + abs(y)
                    # print("tar_x {}, tar_y {}, x {}, y {}, d {}".format(tar_x, tar_y, x, y, d))
                    ans = max(ans, d)

        return ans



# class Solution:
#
#     def maxDistance(self, s: str, k: int) -> int:
#
#         x = 0
#         y = 0
#         xd = {"N": 0, "S": 0, "W": -1, "E": 1}
#         yd = {"N": 1, "S": -1, "W": 0, "E": 0}
#         max_d = -inf
#         max_x = None
#         max_y = None
#         for c in s:
#             x += xd[c]
#             y += yd[c]
#             d = abs(x) + abs(y)
#             if d > max_d:
#                 max_x, max_y = x, y
#                 max_d = d
#
#         print("max_d {}, max_x {}, max_y {}".format(max_d, max_x, max_y))
#         tar_xs = ["W", "E"] if max_x == 0 else (["W"] if max_x > 0 else ["E"])
#         tar_ys = ["S", "N"] if max_y == 0 else (["S"] if max_y > 0 else ["N"])
#         print("tar_xs {}, tar_ys {}".format(tar_xs, tar_ys))
#
#         od = {"W": "E", "E": "W", "S": "N", "N": "S"}
#         ans = max_d
#         for tar_x in tar_xs:
#             for tar_y in tar_ys:
#                 x = 0
#                 y = 0
#                 for i, _ in enumerate(s):
#                     c = s[i]
#                     if k and (c == tar_x or c == tar_y):
#                         c = od[c]
#                         k -= 1
#                     x += xd[c]
#                     y += yd[c]
#                     d = abs(x) + abs(y)
#                     print("tar_x {}, tar_y {}, x {}, y {}, d {}".format(tar_x, tar_y, x, y, d))
#                     ans = max(ans, d)
#
#         return ans







# class Solution:
#
#     def maxDistance(self, s: str, k: int) -> int:
#
#         n = len(s)
#         xd = {"N": 0, "S": 0, "W": -1, "E": 1}
#         yd = {"N": 1, "S": -1, "W": 0, "E": 0}
#         ans = -inf
#
#         @cache
#         def f(idx, left, x, y):
#
#             nonlocal ans
#
#             if idx >= n:
#                 return
#
#             c = s[idx]
#             if left == 0:
#                 xx = x + xd[c]
#                 yy = y + yd[c]
#                 gain = abs(x) + abs(y) - (abs(xx) + abs(yy))
#                 ans = max(ans, abs(xx) + abs(yy))
#                 f(idx + 1, left, xx, yy)
#                 return
#             else:
#                 for cc in ["N", "S", "W", "E"]:
#                     new_left = left if c == cc else left - 1
#                     xx = x + xd[cc]
#                     yy = y + yd[cc]
#                     ans = max(ans, abs(xx) + abs(yy))
#                     f(idx + 1, new_left, xx, yy)
#                 return
#
#         f(0, k, 0, 0)
#
#         return ans



# class Solution:
#
#     def maxDistance(self, s: str, k: int) -> int:
#
#         cnt = Counter(s)
#         x = 0
#         y = 0
#         xd = {"N": 0, "S": 0, "W": -1, "E": 1,}
#         yd = {"N": 1, "S": -1, "W": 0, "E": 0, }
#         for c in s:
#             x += xd[c]
#             y += yd[c]
#
#         tar_x = "E" if y == 0 else ("W" if x > 0 else "E")
#         tar_y = "N" if x == 0 else ("S" if y > 0 else "N")
#
#         to_add = min(cnt[tar_x] + cnt[tar_y], k)
#         print("x {}, y {}, tar_x {}, tar_y {}, to_add {}".format(x, y, tar_x, tar_y, to_add))
#         return abs(x) + abs(y) + to_add
