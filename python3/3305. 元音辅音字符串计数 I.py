class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:

        n = len(word)
        count = {key: 0 for key in "aeiou"}
        prefix = {-1: 0}
        for idx, char in enumerate(word):
            if char in "aeiou":
                prefix[idx] = prefix[idx - 1]
            else:
                prefix[idx] = prefix[idx - 1] + 1

        left, right = 0, 0
        result = 0
        while left <= n - k - 5:
            while right < n:
                if word[right] in "aeiou":
                    count[word[right]] += 1
                other_count = prefix[right] - prefix[left-1]
                if other_count > k:
                    break
                if all([i >= 1 for i in count.values()]) and other_count == k:
                    # print(left, right, "success")
                    result += 1
                right += 1

            left += 1
            right = left
            count = {key: 0 for key in "aeiou"}
            # if word[left] in "aeiou":
            #     count[word[left]] -= 1
            # left += 1

            # if right > left:
            #     right -= 1
            #     if word[right] in "aeiou":
            #         count[word[right]] -= 1

        return result


if __name__ == '__main__':

    foo = Solution()
    result = foo.countOfSubstrings("aaeuoiouee", 0)
    print(result)
