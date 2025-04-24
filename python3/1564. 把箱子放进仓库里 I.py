class Solution:

    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort()
        hs = list()
        for h in warehouse:
            if not hs:
                hs.append(h)
            else:
                hs.append(min(hs[-1], h))
        ans = 0
        idx = 0
        for h in hs[::-1]:
            box = boxes[idx]
            if box <= h:
                ans += 1
                idx += 1
                if idx >= len(boxes):
                    break

        return ans
