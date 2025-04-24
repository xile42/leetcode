class Solution:

    def minOperations(self, boxes: str) -> List[int]:

        idxs = [idx for idx, num in enumerate(boxes) if num == "1"]
        results = list()

        for idx in range(len(boxes)):
            result = sum([abs(jdx-idx) for jdx in idxs])
            results.append(result)

        return results

