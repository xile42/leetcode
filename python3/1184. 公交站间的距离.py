class Solution:

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        if start > destination:
            start, destination = destination, start

        s = sum(distance)
        acc = [0] + list(accumulate(distance))
        ans1 = acc[destination] - (0 if start == 0 else acc[start])
        ans2 = s - ans1

        return min(ans1, ans2)
