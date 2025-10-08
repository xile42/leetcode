class Solution:

    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:

        h1, m1 = map(int, loginTime.split(":"))
        h2, m2 = map(int, logoutTime.split(":"))

        if h1 > h2 or (h1 == h2 and m1 > m2):
            h2 += 24

        m1 = ceil(m1 / 15) * 15
        m2 = floor(m2 / 15) * 15
        if m1 == 60:
            m1 = 0
            h1 += 1
        if m2 == 60:
            m2 = 0
            h2 += 1

        if h1 > h2 or (h1 == h2 and m1 > m2):
            return 0

        ans = 0
        while not (m1 == m2 and h1 == h2):
            m1 += 15
            if m1 == 60:
                m1 = 0
                h1 += 1
            ans += 1

        return ans
