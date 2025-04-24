class Solution:
    
    def getWinner(self, arr: List[int], k: int) -> int:

        mx = arr[0]
        count = 0
        for i in arr[1:]:
            if i > mx:
                mx = i
                count = 0
            count += 1
            if count == k:
                break

        return mx
