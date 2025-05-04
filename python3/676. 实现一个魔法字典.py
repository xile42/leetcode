class MagicDictionary:

    def __init__(self):

        self.d = set()
        self.dd = defaultdict(set)

    def buildDict(self, dictionary: List[str]) -> None:

        for s in dictionary:
            for idx in range(len(s)):
                self.d.add(s[:idx] + "@" + s[idx + 1:])
                self.dd[s[:idx] + "@" + s[idx + 1:]].add(s[idx])

    def search(self, searchWord: str) -> bool:

        s = searchWord
        for idx in range(len(s)):
            if s[:idx] + "@" + s[idx + 1:] in self.d:
                if len(self.dd[s[:idx] + "@" + s[idx + 1:]] - {s[idx]}) != 0:
                    return True

        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)