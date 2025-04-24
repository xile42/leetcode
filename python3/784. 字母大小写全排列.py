class Solution:

    def letterCasePermutation(self, s: str) -> List[str]:

        def f(s, cur):

            if len(s) == 0:
                results.append(cur)
                return

            char = s[0]
            if char.isalpha():
                f(s[1:], cur+char.lower())
                f(s[1:], cur+char.upper())
            else:
                f(s[1:], cur+char)

        results = list()
        f(s, "")

        return results
