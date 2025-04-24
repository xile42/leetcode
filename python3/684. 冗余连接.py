class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        n = len(edges)
        nums = [i for i in range(n + 1)]

        def union(i, j):
            nums[find(j)] = find(i)
            

        def find(i):
            current = i
            if nums[current] != current:
                nums[current] = find(nums[current])

            return nums[current]

        for i, j in edges:
            if find(i) != find(j):
                union(i, j)
            else:
                return [i, j]
        
