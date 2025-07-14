class Solution:

    def maximumGain(self, s: str, x: int, y: int) -> int:

        def f(s, tar, score):

            ans = 0
            st = list()
            for c in s:
                if not st:
                    st.append(c)
                    continue
                if c == tar[-1] and st[-1] == tar[0]:
                    st.pop()
                    ans += score
                    continue
                else:
                    st.append(c)

            return st, ans


        st = list(s)

        if x > y:
            st, ans1 = f(st, "ab", x)
            st, ans2 = f(st, "ba", y)
        else:
            st, ans1 = f(st, "ba", y)
            st, ans2 = f(st, "ab", x)

        return ans1 + ans2
