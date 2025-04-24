class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        def f(a, b):

            va = len(arr2) + a if a not in arr2 else arr2.index(a)
            vb = len(arr2) + b if b not in arr2 else arr2.index(b)

            return va - vb

        return sorted(arr1, key=cmp_to_key(f))
