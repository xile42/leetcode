class Solution:

    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:

        round = min((mainTank - 1) // (5 - 1), additionalTank)
        return (mainTank + round) * 10