class Solution:

    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:

        n = len(arrival)
        ans = [0] * n
        in_queue = deque()
        out_queue = deque()

        idx = 0
        last = 0
        for cur in range(2 * 10 ** 5 + 1):

            if idx >= n and not in_queue and not out_queue:
                break

            while idx < n and arrival[idx] <= cur:
                if state[idx] == 0:
                    in_queue.append(idx)
                else:
                    out_queue.append(idx)
                idx += 1

            if not in_queue and not out_queue:
                last = 0
                continue

            if last == 0 or last == 1:
                if out_queue:
                    guy = out_queue.popleft()
                    ans[guy] = cur
                    last = 1
                else:
                    guy = in_queue.popleft()
                    ans[guy] = cur
                    last = 2
            else:
                if in_queue:
                    guy = in_queue.popleft()
                    ans[guy] = cur
                    last = 2
                else:
                    guy = out_queue.popleft()
                    ans[guy] = cur
                    last = 1

        return ans
