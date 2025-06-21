class Solution:

    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        if len(barcodes) < 2:
            return barcodes

        c = Counter(barcodes)
        ans = [-1] * len(barcodes)
        h = [[-v, k] for k, v in c.items()]
        heapify(h)

        for i in range(len(barcodes) // 2):
            v1, k1 = heappop(h)
            v2, k2 = heappop(h)
            v1 = -v1
            v2 = -v2
            if i > 0 and k1 == ans[i * 2 - 1]:
                v1, k1, v2, k2 = v2, k2, v1, k1
            ans[i * 2] = k1
            ans[i * 2 + 1] = k2
            if v1 > 1:
                heappush(h, [-(v1 - 1), k1])
            if v2 > 1:
                heappush(h, [-(v2 - 1), k2])

        if h:
            ans[-1] = h[0][-1]

        return ans
