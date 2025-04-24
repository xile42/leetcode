class Solution:

    def findWords(self, words: List[str]) -> List[str]:

        s = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        s = [set(i) for i in s]
        results = list()
        for word in words:
            sw = set(word.lower())
            for si in s:
                if len(sw - si) == 0:
                    results.append(word)

        return results
        
