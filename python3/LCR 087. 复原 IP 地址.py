class Solution:

    results = None

    def search(self, s, used, chance):

        if chance == 0:
            if len(s) == 0:
                self.results.append("{}.{}.{}.{}".format(*used))
            return

        if len(s) > 3 * chance or len(s) < chance:
            return

        if len(s) > 0:
            self.search(s[1:], used+[s[0]], chance-1)

        if len(s) > 1 and s[0] != "0":
            self.search(s[2:], used+[s[:2]], chance-1)

        if len(s) > 2 and s[0] != "0":
            value = int(s[:3])
            if 0 <= value <= 255:
                self.search(s[3:], used+[s[:3]], chance-1)

    def restoreIpAddresses(self, s: str) -> List[str]:

        self.results = list()
        self.search(s, list(), 4)
        return self.results
