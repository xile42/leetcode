class Solution:

    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        learned = list(map(set, languages))

        todo_list = []
        for u, v in friendships:
            if learned[u - 1].isdisjoint(learned[v - 1]):
                todo_list.append((u - 1, v - 1))

        ans = inf
        for k in range(1, n + 1):
            st = set()
            for u, v in todo_list:
                if k not in learned[u]:
                    st.add(u)
                if k not in learned[v]:
                    st.add(v)
            ans = min(ans, len(st))

        return ans
