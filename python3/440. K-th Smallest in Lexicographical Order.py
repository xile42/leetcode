class Solution(object):

    def findKthNumber(self, n, k):

        def count_steps(n, curr_prefix, next_prefix):
            steps = 0
            while curr_prefix <= n:
                steps += min(n + 1, next_prefix) - curr_prefix
                curr_prefix *= 10
                next_prefix *= 10
            return steps

        curr = 1
        k -= 1  # We are starting with the first number
        while k > 0:
            steps = count_steps(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr