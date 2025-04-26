class Solution:

    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:

        g = [[] for _ in nums]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        ans = (-1, 0)
        dis = [0]
        last_depth = {}

        @cache
        def dfs(x: int, fa: int, top_depth: int, chance) -> None:

            color = nums[x]
            old_depth = last_depth.get(color, [0, 0])  # 最近的，第二近的
            top_depth1 = max(top_depth, old_depth[0])
            top_depth2 = max(top_depth, old_depth[1])
            nonlocal ans
            if chance:  # 用chance
                ans = max(ans, (dis[-1] - dis[top_depth2], top_depth2 - len(dis)))
            else:
                ans = max(ans, (dis[-1] - dis[top_depth1], top_depth1 - len(dis)))

            last_depth[color] = [len(dis), old_depth[0]]  # 最近的，第二近的
            for y, w in g[x]:
                if y != fa:
                    dis.append(dis[-1] + w)
                    dfs(y, x, top_depth1, chance)
                    if chance and top_depth2 < top_depth1:
                        dfs(y, x, top_depth2, chance - 1)
                    dis.pop()
            last_depth[color] = old_depth

        dfs(0, -1, 0, 1)

        return [ans[0], -ans[1]]
