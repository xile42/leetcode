class Solution:

    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:

##        df(i, j)
##        df(0, ..) = 0
##        df(i, j) = max(df(i-1, 1-j), df(i-1, j) + E[j])

        n = len(energyDrinkA)
        f = [[0, 0] for _ in range(n+1)]
        for t in range(1, n+1):
            f[t][0] = max(f[t-1][1], f[t-1][0] + energyDrinkA[t-1])
            f[t][1] = max(f[t-1][0], f[t-1][1] + energyDrinkB[t-1])

        return max(f[n][0], f[n][1])            
