class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        s = set(arr2)
        ns = [i for i in arr1 if i in s]
        tail = sorted([i for i in arr1 if i not in s])
        ns.sort(key=lambda x: arr2.index(x))

        return ns + tail
