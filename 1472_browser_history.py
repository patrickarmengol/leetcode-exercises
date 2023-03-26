class BrowserHistory:

    def __init__(self, homepage: str):
        self.bs: list[str] = []
        self.fs: list[str] = []
        self.cur: str = homepage

    def visit(self, url: str) -> None:
        self.fs = []
        self.bs.append(self.cur)
        self.cur = url

    def back(self, steps: int) -> str:
        steps = min(steps, len(self.bs))
        for _ in range(steps):
            self.fs.append(self.cur)
            self.cur = self.bs.pop()
        return self.cur

    def forward(self, steps: int) -> str:
        steps = min(steps, len(self.fs))
        for _ in range(steps):
            self.bs.append(self.cur)
            self.cur = self.fs.pop()
        return self.cur


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
