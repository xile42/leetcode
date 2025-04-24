class Solution:

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix_map = dict()
        prefix_map[-1] = 0
        xor_num = 0
        for idx, num in enumerate(arr):
            xor_num ^= num
            prefix_map[idx] = xor_num

        results = list()
        for start, end in queries:
            result = prefix_map[start-1] ^ prefix_map[end]
            results.append(result)

        return results
