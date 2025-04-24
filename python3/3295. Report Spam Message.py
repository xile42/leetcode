class Solution:

    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:

        ban_set = set(bannedWords)
        count = 0
        for word in message:
            if word in ban_set:
                count += 1
                if count >= 2:
                    return True

        return False
