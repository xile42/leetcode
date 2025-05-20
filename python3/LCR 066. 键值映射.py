class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = dict()
        self.prefix = defaultdict(list)

    def insert(self, key: str, val: int) -> None:

        if key not in self.d:
            for i in range(1, len(key) + 1):
                self.prefix[key[:i]].append(key)
        self.d[key] = val

    def sum(self, prefix: str) -> int:

        ans = 0
        for key in self.prefix[prefix]:
            ans += self.d[key]

        return ans



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)