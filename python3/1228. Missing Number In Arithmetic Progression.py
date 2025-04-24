from collections import defaultdict


class Solution:
    
    def missingNumber(self, arr: List[int]) -> int:

        flag = -1 if arr[1] < arr[0] else 1

        count = defaultdict(list)
        for i in range(len(arr)-1):
            count[abs(arr[i+1]-arr[i])].append(i)

        return arr[count[max(count.keys())][0]] + max(count.keys()) // 2 * flag
        
