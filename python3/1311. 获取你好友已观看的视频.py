class Solution:

    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:

        n = len(watchedVideos)
        vis = [False] * n
        dis = [0] * n

        q = list()
        q.append(id)
        vis[id] = True
        cur_dis = 1
        while q:
            next_q = list()
            for i in q:
                for j in friends[i]:
                    if vis[j]:
                        continue
                    vis[j] = True
                    dis[j] = cur_dis
                    next_q.append(j)
            q = next_q
            cur_dis += 1
            if cur_dis > level:
                break

        ns = list()
        for i in range(n):
            if dis[i] == level:
                ns += watchedVideos[i]

        return [i[1] for i in sorted([[v, k] for k, v in Counter(ns).items()])]
