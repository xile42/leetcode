class Solution:

    def angleClock(self, hour: int, minutes: int) -> float:

        h_deg = 360 / 12 * hour
        m_deg = 360 / 60 * minutes
        h_deg += minutes / 60 * (360 / 12)

        ans1 = abs(h_deg - m_deg)
        ans2 = 360 - ans1

        return min(ans1, ans2)
