class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:

        # dp[i]: 最大位数 for cost i, -1 means unreachable
        dp = [-1] * (target + 1)
        dp[0] = 0  # 0 cost has 0 digits

        for i in range(1, target + 1):
            max_digits = -1
            for d in range(9):  # d: 0 to 8, representing digit 1 to 9
                c = cost[d]
                if i >= c and dp[i - c] != -1:
                    # Update max_digits if using digit d+1 gives more digits
                    if dp[i - c] + 1 > max_digits:
                        max_digits = dp[i - c] + 1
            dp[i] = max_digits  # Store the result for cost i

        # If target is unreachable, return "0"
        if dp[target] == -1:
            return "0"

        # Build the largest number string greedily
        res = []  # Result characters
        rem = target  # Remaining cost
        while rem > 0:
            found = False
            # Try digits from 9 to 1 (d index from 8 down to 0)
            for d in range(8, -1, -1):
                digit = d + 1  # Actual digit (1-9)
                c = cost[d]  # Cost of this digit
                # Check if we can use this digit and the remainder is valid
                if rem >= c and dp[rem - c] != -1:
                    # Using this digit should reduce the digit count by 1
                    if dp[rem - c] == dp[rem] - 1:
                        res.append(str(digit))
                        rem -= c
                        found = True
                        break  # Break inner loop after choosing the largest valid digit
            if not found:
                # Should not happen if dp is correct, but safe guard
                break

        return ''.join(res)
