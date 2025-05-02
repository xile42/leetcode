class Solution:

    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word

        length = len(word) - numFriends + 1
        ans = None
        for left in range(len(word)):
            cur = word[left:left+length]
            # if len(cur) < length:
            #     break
            if ans is None or cur > ans:
                ans = cur

        return ans
