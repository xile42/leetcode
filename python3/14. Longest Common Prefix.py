class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        result = 0
        max_result = min([len(i) for i in strs])

        for idx in range(max_result):
            chars = set([i[idx] for i in strs])
            if len(chars) == 1:
                result += 1
            else:
                break

        return strs[0][:result]
