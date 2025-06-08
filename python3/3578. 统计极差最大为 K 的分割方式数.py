def mx(a, b):
    return a if a > b else b

def mn(a, b):
    return a if a < b else b


class Solution:

    def countPartitions(self, nums: List[int], k: int) -> int:

        # # 超时
        # mod = pow(10, 9) + 7
        # n = len(nums)
        #
        # @cache
        # def f(i):
        #
        #     if i >= n:
        #         return 1
        #
        #     ans = 0
        #     cur_mx = -inf
        #     cur_mn = inf
        #     for j in range(i, n):
        #         v = nums[j]
        #         cur_mx = mx(cur_mx, v)
        #         cur_mn = mn(cur_mn, v)
        #         if cur_mx - cur_mn <= k:
        #             ans += f(j + 1) % mod
        #             ans %= mod
        #         else:
        #             break
        #     print("f({}) = {}".format(i, ans))
        #     return ans
        #
        # ans = f(0)
        # f.cache_clear()
        #
        # return ans % mod

        mod = pow(10, 9) + 7
        n = len(nums)

        pre = [0] * (n + 3)
        pre[0] = 0
        pre[1] = 1
        l = 0
        max_queue = deque()
        min_queue = deque()

        for i in range(n):
            while max_queue and nums[max_queue[-1]] <= nums[i]:
                max_queue.pop()
            max_queue.append(i)

            while min_queue and nums[min_queue[-1]] >= nums[i]:
                min_queue.pop()
            min_queue.append(i)

            while max_queue and min_queue and nums[max_queue[0]] - nums[min_queue[0]] > k:
                if max_queue[0] == l:
                    max_queue.popleft()
                if min_queue[0] == l:
                    min_queue.popleft()
                l += 1

            dp_i = (pre[i + 1] - pre[l]) % mod
            if dp_i < 0:
                dp_i += mod
            pre[i + 2] = (pre[i + 1] + dp_i) % mod

        return dp_i % mod
