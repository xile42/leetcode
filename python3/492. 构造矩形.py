class Solution:

    def constructRectangle(self, area: int) -> List[int]:

        for l in range(ceil(sqrt(area)), area + 1):
            if area % l == 0:
                return [l, area // l]
