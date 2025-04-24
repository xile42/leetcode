class Solution:

    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        t = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        d = {idx: value for idx, value in enumerate(t)}
        results = list()
        for word in words:
            results.append("".join([d[ord(char) - ord("a")] for char in word]))

        return len(set(results))
