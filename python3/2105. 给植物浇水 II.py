class Solution:

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:

        ans = 0
        left = 0
        right = len(plants) - 1
        cura = capacityA
        curb = capacityB
        while left <= right:
            if left == right:
                if max(cura, curb) < plants[left]:
                    ans += 1
                break
            if cura >= plants[left]:
                cura -= plants[left]
            else:
                ans += 1
                cura = capacityA - plants[left]
            if curb >= plants[right]:
                curb -= plants[right]
            else:
                ans += 1
                curb = capacityB - plants[right]
            left += 1
            right -= 1

        return ans
