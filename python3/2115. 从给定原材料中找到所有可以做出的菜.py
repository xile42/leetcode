class Solution:

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        indegrees = defaultdict(int)
        s = set(supplies)
        sr = set(recipes)
        g = defaultdict(list)
        for i, vs in enumerate(ingredients):
            u = recipes[i]
            for v in vs:
                indegrees[u] += 1
                g[v].append(u)

        ans = set([i for i in supplies if i in sr])
        q = deque([v for v in recipes if indegrees[v] == 0] + supplies)
        while q:
            u = q.popleft()
            if u in sr:
                ans.add(u)
            for v in g[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    q.append(v)
                    ans.add(v)

        return list(ans)
