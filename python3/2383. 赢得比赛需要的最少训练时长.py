class Solution:

    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:

        cur_energy, cur_exp = initialEnergy, initialExperience
        ans = 0
        for enemy_energy, enemy_exp in zip(energy, experience):
            ans += max((enemy_energy + 1) - cur_energy, 0)
            ans += max((enemy_exp + 1) - cur_exp, 0)
            cur_energy = max(enemy_energy + 1, cur_energy) - enemy_energy
            cur_exp = max(enemy_exp + 1, cur_exp) + enemy_exp

        return ans
