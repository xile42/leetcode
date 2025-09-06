class NumberContainers:

    def __init__(self):

        self.m = dict()
        self.ms = defaultdict(list)

    def change(self, index: int, number: int) -> None:

        self.m[index] = number
        heappush(self.ms[number], index)  # 直接添加新数据，后面 find 再删除旧的

    def find(self, number: int) -> int:

        h = self.ms[number]
        while h and self.m[h[0]] != number:  # 意味着 h[0] 处的元素已被替换成了其他值
            heappop(h)

        return h[0] if h else -1
