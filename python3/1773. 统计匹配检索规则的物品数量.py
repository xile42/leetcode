class Solution:

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        d = dict()
        d["type"], d["color"], d["name"] = zip(*items)
        n = len(d["type"])
        ans = 0
        for i in range(n):
            if d[ruleKey][i] == ruleValue:
                ans += 1

        return ans
