class Solution:

    def concatHex36(self, n: int) -> str:

        d16 = [str(i) for i in range(10)] + [chr(ord("A") + i) for i in range(6)]
        d36 = [str(i) for i in range(10)] + [chr(ord("A") + i) for i in range(26)]

        def f(x, k, d):

            ans = list()
            while x:
                i = x % k
                ans.append(d[i])
                x //= k

            return "".join(ans[::-1])

        return f(n ** 2, 16, d16) + f(n ** 3, 36, d36)
