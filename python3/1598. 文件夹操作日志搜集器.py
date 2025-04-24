class Solution:

    def minOperations(self, logs: List[str]) -> int:

        cnt = 0
        for i in logs:
            if i == "../":
                cnt = max(cnt - 1, 0)
            elif i == "./":
                continue
            else:
                cnt += 1

        return cnt
