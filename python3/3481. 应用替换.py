class Solution:

    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:

        s = text
        while "%" in s:
            for k, v in replacements:
                s = s.replace("%" + k + "%", v)

        return s
