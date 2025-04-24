class Solution:

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()
        diffs = [[arr[i] - arr[i - 1], [arr[i - 1], arr[i]]] for i in range(1, len(arr))]
        diffs.sort(key=lambda x: x[0])
        v = diffs[0][0]
        ans = [i[1] for i in diffs if i[0] == v]
        ans.sort()

        return ans
