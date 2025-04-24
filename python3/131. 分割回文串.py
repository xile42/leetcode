class Solution:

    def partition(self, s: str) -> List[List[str]]:

        results = list()        

        def f(s, cur):

            if len(s) == 0:
                results.append(cur)
                return

            start = 0
            for end in range(1, len(s) + 1):
                ss = s[start:end]
                if ss == ss[::-1]:
                    f(s[end:], cur + [ss])

        f(s, [])

        return results
