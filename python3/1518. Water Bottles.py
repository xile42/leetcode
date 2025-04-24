class Solution:

    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        result = 0
        current = numBottles
        while current >= numExchange:
            change = current // numExchange
            result += change
            current = change + current % numExchange

        return result + numBottles
