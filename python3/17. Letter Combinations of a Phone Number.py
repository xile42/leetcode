class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        map = {
            "2": ["a", "b", "c",],
            "3": ["d", "e", "f",],
            "4": ["g", "h", "i",],
            "5": ["j", "k", "l",],
            "6": ["m", "n", "o",],
            "7": ["p", "q", "r", "s",],
            "8": ["t", "u", "v",],
            "9": ["w", "x", "y", "z",],
        }

        result = list()
        for char in digits:
            if len(result) == 0:
                result = map[char]
            else:
                result = [i + j for i in result for j in map[char]]

        return result
