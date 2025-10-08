class Solution:

    def maxDistance(self, words: List[str]) -> int:

        n = len(words)
        ans = list()

        i = 0
        j = n - 1
        while i < j:
            if words[i] != words[j]:
                ans.append(j - i + 1)
                break
            j -= 1

        i = 0
        j = n - 1
        while i < j:
            if words[i] != words[j]:
                ans.append(j - i + 1)
                break
            i += 1

        return 0 if not ans else max(ans)
