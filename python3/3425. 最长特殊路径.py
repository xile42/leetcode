class Solution:

    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:

        g = [[] for _ in nums]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        ans = (-1, 0)
        dis = [0]
        last_depth = {}  # 颜色 -> 该颜色最近一次出现的深度 +1，注意这里已经 +1 了

        def dfs(x: int, fa: int, top_depth: int) -> None:
            color = nums[x]
            old_depth = last_depth.get(color, 0)
            top_depth = max(top_depth, old_depth)

            nonlocal ans
            # 把 len(dis) - top_depth 取反，这样 max 算的是最小值
            ans = max(ans, (dis[-1] - dis[top_depth], top_depth - len(dis)))

            last_depth[color] = len(dis)
            for y, w in g[x]:
                if y != fa:  # 避免访问父节点
                    dis.append(dis[-1] + w)
                    dfs(y, x, top_depth)
                    dis.pop()  # 恢复现场
            last_depth[color] = old_depth  # 恢复现场

        dfs(0, -1, 0)

        return [ans[0], -ans[1]]
