class Solution:

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        ns = sorted(people, key=lambda x: [-x[0], x[1]])
        ans = list()
        for h, k in ns:
            if not ans:
                ans.append([h, k])
            else:
                ans.insert(k, [h, k])

        return ans
