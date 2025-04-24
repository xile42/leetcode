from functools import cmp_to_key


def compare(x, y):

    xy, yx = x + y, y + x
    if xy == yx:
        return 0
    return 1 if xy > yx else -1


class Solution:

    def largestNumber(self, nums: List[int]) -> str:

        str_list = sorted([str(i) for i in nums], key=cmp_to_key(compare), reverse=True)
        result = "".join(str_list)
        if set(result) == {"0"}:
            return "0"
        return result
