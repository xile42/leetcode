class Solution:

    def minArraySum(self, nums: List[int], k: int) -> int:

        n = len(nums)
        pre_sum = [0] * (n + 1)
        pre_mod = [0] * (n + 1)

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            pre_mod[i] = pre_sum[i] % k

        left_arr = [0] * (n + 1)
        l = 0
        freq = defaultdict(int)
        for r in range(n + 1):
            freq[pre_mod[r]] += 1
            while freq[pre_mod[r]] > 1:
                freq[pre_mod[l]] -= 1
                l += 1
            left_arr[r] = l

        dp = [0] * (n + 1)
        min_dp = dict()
        min_dp[pre_mod[0]] = 0
        queue = deque()
        queue.append(0)

        for i in range(1, n + 1):
            op1 = min_dp.get(pre_mod[i], inf)

            while queue and queue[0] < left_arr[i]:
                queue.popleft()
            op2 = inf
            if queue:
                j = queue[0]
                op2 = dp[j] - pre_sum[j] + pre_sum[i]

            dp[i] = min(op1, op2)

            if dp[i] < min_dp.get(pre_mod[i], inf):
                min_dp[pre_mod[i]] = dp[i]

            while queue and dp[queue[-1]] - pre_sum[queue[-1]] >= dp[i] - pre_sum[i]:
                queue.pop()
            queue.append(i)

        return dp[n]
