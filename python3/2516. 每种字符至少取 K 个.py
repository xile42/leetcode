from collections import Counter


class Solution:

    def takeCharacters(self, s: str, k: int) -> int:

        counter = Counter(s)
        if any([counter[i] < k for i in "abc"]):
            return -1

        result = left = 0
        for idx, char in enumerate(s):
            counter[char] -= 1
            while counter[char] < k:
                counter[s[left]] += 1
                left += 1
            result = max(result, idx - left + 1)

        return len(s) - result

        # if k == 0:
        #     return 0
        #
        # n = len(s)
        # idx_dict = {"a": 0, "b": 1, "c": 2}
        # counter_left = [-k, -k, -k]
        # for char in s:
        #     counter_left[idx_dict[char]] += 1
        # for value in counter_left:
        #     if value < 0:
        #         return -1
        #
        # left = 0
        # result = -float("inf")
        #
        # while left < n:
        #
        #     right = left
        #     counter = [0, 0, 0]
        #     while right < n and counter_left[idx_dict[s[right]]] >= counter[idx_dict[s[right]]] + 1:
        #         counter[idx_dict[s[right]]] += 1
        #         right += 1
        #
        #     this_length = right - left
        #     result = max(result, this_length)
        #     left += 1
        #
        #     if n - left < result:
        #         break
        #
        # return n - result

        # if k == 0:
        #     return 0
        #
        # n = len(s)
        # a_indexs = [idx+1 for idx in range(n) if s[idx] == "a"]
        # b_indexs = [idx+1 for idx in range(n) if s[idx] == "b"]
        # c_indexs = [idx+1 for idx in range(n) if s[idx] == "c"]
        #
        # if len(a_indexs) < k or len(b_indexs) < k or len(c_indexs) < k:
        #     return -1
        #
        # a_indexs = [0] + a_indexs + [n+1]
        # b_indexs = [0] + b_indexs + [n+1]
        # c_indexs = [0] + c_indexs + [n+1]
        #
        # result = float("inf")
        # for a_left in range(k+1):
        #     a_right = k - a_left
        #     for b_left in range(k+1):
        #         b_right = k - b_left
        #         for c_left in range(k+1):
        #             c_right = k - c_left
        #             left_result = max(a_indexs[a_left], b_indexs[b_left], c_indexs[c_left])
        #             right_result = max(n-a_indexs[::-1][a_right]+1, n-b_indexs[::-1][b_right]+1, n-c_indexs[::-1][c_right]+1)
        #             this_result = n if left_result + right_result > n else left_result + right_result
        #             result = min(result, this_result)
        #
        # return result
