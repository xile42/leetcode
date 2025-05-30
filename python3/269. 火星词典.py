class Solution:

    def alienOrder(self, words: List[str]) -> str:

        g = [set() for _ in range(26)]
        base = ord("a")
        all_c = set()
        indegree = [0 for _ in range(26)]

        for s1, s2 in pairwise(words):
            if s1 == s2:
                continue
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    g[ord(c1) - base].add(ord(c2) - base)
                    all_c.add(ord(c1) - base)
                    all_c.add(ord(c2) - base)
                    break
            else:
                if len(s1) > len(s2):
                    return str()

        q = deque()
        for i in range(26):
            for j in g[i]:
                indegree[j] += 1

        for i in range(26):
            if i in all_c and indegree[i] == 0:
                q.append(i)

        ans = list()
        while q:
            i = q.popleft()
            ans.append(i)
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

        if len(ans) != len(all_c):
            return str()

        ans = "".join([chr(i + base) for i in ans])
        s = set()
        for w in words:
            s |= set(w)
        for c in s:
            if c not in ans:
                ans += c

        return ans
