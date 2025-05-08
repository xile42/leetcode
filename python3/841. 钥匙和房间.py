class Solution:

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        vis = [False] * n
        vis[0] = True
        q = rooms[0]

        while q:
            cur = q.pop(0)
            if vis[cur]:
                continue
            vis[cur] = True
            q += rooms[cur]

        return sum(vis) == n
