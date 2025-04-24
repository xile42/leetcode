class Solution:

    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:

        counter = defaultdict(int)
        for num in nums1:
            if num % k != 0:
                continue
            t = num // k
            for v in range(1, floor(sqrt(t))+1):
                if t % v != 0:
                    continue
                counter[v] += 1
                another = t // v
                if v != another:
                    counter[another] += 1

        return sum([counter[i] for i in nums2])
