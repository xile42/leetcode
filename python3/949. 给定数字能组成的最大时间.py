class Solution:

    def largestTimeFromDigits(self, arr: List[int]) -> str:

        ans = None
        arr.sort(reverse=True)

        def f(nums, cur, path):

            nonlocal ans
            if ans is not None:
                return

            if cur == 4:
                ans = path
                return

            for i, n in enumerate(nums):
                if cur == 0:
                    if n > 2:
                        continue
                    f(nums[:i] + nums[i + 1:], cur + 1, path + [n])
                elif cur == 1:
                    if path[-1] == 2 and n > 3:
                        continue
                    f(nums[:i] + nums[i + 1:], cur + 1, path + [n])
                elif cur == 2:
                    if n > 5:
                        continue
                    f(nums[:i] + nums[i + 1:], cur + 1, path + [n])
                else:
                    f(nums[:i] + nums[i + 1:], cur + 1, path + [n])

        f(arr, 0, list())

        return str() if ans is None else "{}{}:{}{}".format(*ans)
