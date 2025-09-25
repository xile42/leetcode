class Solution:

    def prevPermOpt1(self, arr: List[int]) -> List[int]:

        n = len(arr)
        if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
            return arr

        c = Counter()
        for i in range(n - 1, -1, -1):
            v = arr[i]
            if c and min(c) < v:
                mv = max(k for k in c if k < v)
                for j in range(i + 1, n):
                    if arr[j] == mv:
                        arr[i], arr[j] = arr[j], arr[i]
                        return arr
            c[v] += 1
