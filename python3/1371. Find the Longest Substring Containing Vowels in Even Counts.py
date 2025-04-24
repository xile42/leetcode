class Solution:

    def findTheLongestSubstring(self, s: str) -> int:

        mask_dict = dict()
        mask = 0
        mask_dict[-1] = mask
        idx_map = {"a": 5, "e": 4, "i": 3, "o": 2, "u": 1}
        for idx, char in enumerate(s):
            if char in idx_map:
                mask ^= 1 << idx_map[char]
            mask_dict[idx] = mask

        result = 0
        for idx in range(len(s)):
            for jdx in range(len(s)-1, idx-1, -1):
                value = (mask_dict[jdx] ^ mask_dict[idx-1]).bit_count()

                if value == 0:
                    result = max(result, jdx-idx+1)
                    break

        return result
