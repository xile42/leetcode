class Solution:

    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:

        if currentEnergy < min(enemyEnergies):
            return 0

        return (sum(enemyEnergies) - min(enemyEnergies) + currentEnergy) // min(enemyEnergies)
