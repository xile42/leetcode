class Solution:

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        cur = heights[0]
        total = 0
        heap = list()
        ladders_total = 0

        for i, h in enumerate(heights):
            if i == 0:
                continue
            if h <= cur:
                cur = h
                continue
            total += h - cur
            if not heap:
                if ladders > 0:
                    heappush(heap, h - cur)
                    ladders_total += h - cur
            elif len(heap) < ladders:
                heappush(heap, h - cur)
                ladders_total += h - cur
            elif heap[0] < h - cur:
                ladders_total += h - cur - heappop(heap)
                heappush(heap, h - cur)

            need = total - ladders_total
            if need > bricks:
                return i - 1
            cur = h

        return len(heights) - 1
