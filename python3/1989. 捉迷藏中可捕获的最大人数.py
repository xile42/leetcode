class Solution:

    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:

        n = len(team)
        diff = [0] * (n + 1)  # 差分数组

        for i, v in enumerate(team):
            if v == 1:  # 更新捕捉范围
                diff[max(i - dist, 0)] += 1
                diff[min(i + dist + 1, n)] -= 1

        ans = 0
        ns = list(accumulate(diff))  # 有多少个鬼能抓到该位置

        for catched, v in zip(ns, team):
            if catched and v == 0:
                ans += 1

        return min(ans, team.count(1))  # 每个鬼只能抓一个，但这里隐含了，ns[i] > 0，则i位置一定能被抓到，而不需要考虑谁抓谁怎么分配
