class Solution:

    def stableMountains(self, height: List[int], threshold: int) -> List[int]:

        results = list()
        for idx in range(len(height)-1):
            value = height[idx]
            if value > threshold:
                results.append(idx+1)

        return results
