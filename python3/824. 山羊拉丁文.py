class Solution:

    def toGoatLatin(self, sentence: str) -> str:

        results = list()
        valid = "aeiouAEIOU"
        for idx, word in enumerate(sentence.split(" ")):
            char = word[0]
            if char in valid:
                results.append(word+"ma"+("a"*(idx+1)))
            else:
                results.append(word[1:]+word[0]+"ma"+("a"*(idx+1)))

        return " ".join(results)
