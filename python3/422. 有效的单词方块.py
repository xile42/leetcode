class Solution:

    def validWordSquare(self, words: List[str]) -> bool:

        n = len(words)
        for k in range(n):
            if words[k] != "".join([i[k] for i in words if len(i) > k]):
                return False

        return True
