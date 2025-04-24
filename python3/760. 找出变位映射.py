class Solution:

    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = defaultdict(list)
        for i, n in enumerate(nums2):
            d[n].append(i)

        ans = list()
        for n in nums1:
            ans.append(d[n].pop(-1))

        return ans
