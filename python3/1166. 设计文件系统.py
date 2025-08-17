class FileSystem:

    def __init__(self):

        self.d = dict()

    def createPath(self, path: str, value: int) -> bool:

        parts = path.strip().split("/")
        if tuple(parts) in self.d:
            return False
        pre = parts[:-1]
        if len(pre) == 1 or tuple(pre) in self.d:
            self.d[tuple(parts)] = value
            return True
        else:
            return False

    def get(self, path: str) -> int:

        parts = path.strip().split("/")
        if tuple(parts) in self.d:
            return self.d[tuple(parts)]
        else:
            return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)