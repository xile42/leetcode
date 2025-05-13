class Solution:

    def dividePlayers(self, skill: List[int]) -> int:

        ans = 0
        skill.sort()
        s = skill[0] + skill[-1]
        n = len(skill)
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != s:
                return -1
            ans += skill[i] * skill[n - 1 - i]

        return ans
