class Solution:

    results = None

    def search(self, length, current):

        if length == 1:
            self.results.append(current+"1")
            self.results.append(current+"0")
            return

        if length == 0:
            self.results.append(current)
            return

        # 1
        self.search(length-1, current+"1")
        # 0
        self.search(length-2, current+"01")

    def validStrings(self, n: int) -> List[str]:

        self.results = list()
        self.search(n, str())

        return self.results
