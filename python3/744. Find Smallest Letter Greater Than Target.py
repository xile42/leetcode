# from string import ascii_lowercase
#
#
# class Solution:
#
#     char_map = {char: idx for idx, char in enumerate(ascii_lowercase)}
#
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
#
#         int_letters = [self.char_map[i] for i in letters]
#         int_target = self.char_map[target]
#         left, right = 0, len(int_letters)-1
#         while left <= right:
#             mid = left + (right-left) // 2
#             if int_letters[mid] <= int_target:
#                 left = mid + 1
#             else:
#                 if mid == 0:
#                     return letters[mid]
#                 if int_letters[mid-1] <= int_target:
#                     return letters[mid]
#                 right = mid - 1
#
#         if left >= len(letters) or int_letters[left] <= int_target:
#             return letters[0]
#
#         return letters[left]


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1

        if target >= letters[-1]:
            return letters[0]

        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return letters[l]
