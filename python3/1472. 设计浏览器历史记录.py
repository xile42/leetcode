class BrowserHistory:

    def __init__(self, homepage: str):

        self.cur = homepage
        self.b = []
        self.f = []
        

    def visit(self, url: str) -> None:

        self.f = []
        self.b.append(self.cur)
        self.cur = url

    def back(self, steps: int) -> str:

        for _ in range(steps):
            if not self.b:
                break
            self.f.append(self.cur)
            self.cur = self.b.pop(-1)

        return self.cur
            
    def forward(self, steps: int) -> str:

        for _ in range(steps):
            if not self.f:
                break
            self.b.append(self.cur)
            self.cur = self.f.pop(-1)

        return self.cur
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
