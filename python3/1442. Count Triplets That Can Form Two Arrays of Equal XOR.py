class Solution:

    def countTriplets(self, arr: List[int]) -> int:

        prefixs = dict()
        prefixs[-1] = 0

        xor_value = 0
        for idx, value in enumerate(arr):
            xor_value ^= value
            prefixs[idx] = xor_value

        results = 0
        for idx in range(len(arr)-1):
            for jdx in range(idx+1, len(arr)):
                xor_ij = prefixs[idx-1] ^ prefixs[jdx-1]
                for kdx in range(jdx, len(arr)):
                    xor_jk = prefixs[jdx-1] ^ prefixs[kdx]
                    if xor_ij == xor_jk:
                        results += 1

        return results
