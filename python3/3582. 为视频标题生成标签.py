class Solution:

    def generateTag(self, caption: str) -> str:

        words = caption.split(" ")
        words = [w for w in words if w]

        if not words:
            return "#"

        ans = list()
        ans.append("#")

        ans.append(words[0].lower())
        for w in words[1:]:
            w = w.capitalize()
            ans.append(w)

        return "".join(ans)[:100]
