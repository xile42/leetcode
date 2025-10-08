class Solution:

    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:

        if nums1 == nums2:
            return 0

        n = len(nums1)
        vis = set()
        queue = deque()
        start = tuple(nums1)
        vis.add(start)
        queue.append((start, 0))

        while queue:

            ns, steps = queue.popleft()
            if list(ns) == nums2:
                return steps

            for l in range(len(ns)):
                for r in range(l, len(ns)):
                    mid = ns[l:r + 1]
                    pre = ns[:l]
                    suf = ns[r + 1:]
                    base = pre + suf
                    for pos in range(len(base) + 1):
                        new_ns = base[:pos] + mid + base[pos:]
                        tuple_ns = tuple(new_ns)
                        if tuple_ns not in vis:
                            vis.add(tuple_ns)
                            queue.append((tuple_ns, steps + 1))
