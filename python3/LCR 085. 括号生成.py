class Solution:

    results = list()

    def dfs(self, s: str, chance, left_remain, right_remain):

        if left_remain == 0 and right_remain == 0:
            self.results.append(s)
            return

        if chance > 0:
            self.dfs(s+")", chance-1, left_remain, right_remain-1)

        if left_remain > 0:
            self.dfs(s+"(", chance+1, left_remain-1, right_remain)

    def generateParenthesis(self, n: int) -> List[str]:

        self.results = list()
        self.dfs(str(), 0, n, n)

        return self.results