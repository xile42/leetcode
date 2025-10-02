class Solution:

    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:

        par = defaultdict(set)
        for region in regions:
            for r in region[1:]:
                par[r].add(region[0])
        c = Counter()

        queue = deque()
        queue.append(region1)
        while queue:
            next_queue = deque()
            for node in queue:
                c[node] = 1
                for p_node in par[node]:
                    if c[p_node] == 0:
                        next_queue.append(p_node)
            queue = next_queue

        cc = Counter()
        queue = deque()
        queue.append(region2)
        while queue:
            next_queue = deque()
            for node in queue:
                cc[node] = 1
                if c[node] == 1:
                    return node
                for p_node in par[node]:
                    if cc[p_node] == 0:
                        next_queue.append(p_node)
            queue = next_queue
