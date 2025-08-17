class Solution:

    def canReach(self, arr: List[int], start: int) -> bool:

        if arr[start] == 0:
            return True

        n = len(arr)
        vis = [False] * n
        queue = deque()
        queue.append(start)

        while queue:
            cur = queue.popleft()
            vis[cur] = True
            if arr[cur] == 0:
                return True

            left = cur - arr[cur]
            if 0 <= left < n and not vis[left]:
                queue.append(left)
            right = cur + arr[cur]
            if 0 <= right < n and not vis[right]:
                queue.append(right)

        return False
