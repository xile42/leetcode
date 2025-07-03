def common_prefix_length(s1, s2):

    min_len = min(len(s1), len(s2))
    for i in range(min_len):
        if s1[i] != s2[i]:
            return i

    return min_len


class Solution:

    def longestCommonPrefix(self, words: List[str]) -> List[int]:

        n = len(words)

        pre = [0] * n
        for i in range(1, n):
            v = common_prefix_length(words[i - 1], words[i])
            pre[i] = max(pre[i - 1], v)

        suf = [0] * n
        for i in range(n - 2, -1, -1):
            v = common_prefix_length(words[i + 1], words[i])
            suf[i] = max(suf[i + 1], v)

        ans = list()
        for i in range(n):
            left = pre[i - 1] if i > 0 else 0
            right = suf[i + 1] if i < n - 1 else 0
            mid = -inf
            if i > 0 and i < n - 1:
                mid = common_prefix_length(words[i - 1], words[i + 1])
            ans.append(max(left, right, mid))

        return ans
