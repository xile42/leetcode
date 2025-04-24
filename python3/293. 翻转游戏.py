class Solution:

    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        result = list()
        for idx in range(len(currentState) - 1):
            if currentState[idx] == currentState[idx + 1] == "+":
                result.append(currentState[:idx] + "--" + currentState[idx+2:])

        return result
        
