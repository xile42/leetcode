class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = "".join([c if c not in "!?',;." else " " for c in paragraph])
        words = [w for w in paragraph.lower().split(" ") if w not in banned and len(w) > 0]
        c = Counter(words)
        kvs = sorted(list(c.items()), key=lambda x: x[-1], reverse=True)

        return kvs[0][0]
