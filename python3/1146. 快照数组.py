class SnapshotArray:

    def __init__(self, length: int):

        self.ns = [[0] for _ in range(length)]
        self.d = defaultdict(lambda: defaultdict(int))
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:

        if self.snap_id != self.ns[index][-1]:
            self.ns[index].append(self.snap_id)
        self.d[index][self.snap_id] = val

    def snap(self) -> int:

        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:

        snap_ids = self.ns[index]
        idx = bisect_right(snap_ids, snap_id)
        if idx == 0:
            return self.d[index][0]
        else:
            return self.d[index][snap_ids[idx - 1]]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)