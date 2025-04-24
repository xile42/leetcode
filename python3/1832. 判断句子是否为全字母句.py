class Solution:

    def checkIfPangram(self, sentence: str) -> bool:

        return len(set(string.ascii_lowercase) - set(sentence)) == 0
