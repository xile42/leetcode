class Solution:

    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        for k, v in knowledge:
            s = s.replace(f"({k})", v)

        ans = list()
        valid = True
        for c in s:
            if c == "(":
                valid = False
            elif c == ")":
                valid = True
                ans.append("?")
            else:
                if valid:
                    ans.append(c)

        return "".join(ans)
