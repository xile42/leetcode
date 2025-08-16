class Solution:

    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:

        marks = list()
        for i, src, tar in zip(indices, sources, targets):
            if src == s[i:i + len(src)]:
                marks.append((i, len(src), tar))
        marks.sort(key=lambda x: x[0])

        ans = list()
        i = 0
        while i < len(s):
            c = s[i]
            if marks and i == marks[0][0]:
                start, length, target = marks.pop(0)
                ans.append(target)
                i += length
            else:
                ans.append(c)
                i += 1

        return "".join(ans)
