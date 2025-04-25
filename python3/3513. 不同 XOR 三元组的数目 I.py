def f(n):

    s = set()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                s.add(i ^ j ^ k)

    return len(s), s

for i in range(1, 70 + 1):
    l, s = f(i)
    print(i, l, s)


# class Solution:
#
#     def uniqueXorTriplets(self, nums: List[int]) -> int:
#
#         n = len(nums)
#         ans = [0, 1, 2, 4, 8]
#         if n < len(ans):
#             return ans[n]
#         l = n.bit_length()
#
#         return 1 << l
#
