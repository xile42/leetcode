class Solution:
    
    def findWinningPlayer(self, skills: List[int], k: int) -> int:

        max_idx = count = 0
        for idx in range(1, len(skills)):
            if skills[idx] > skills[max_idx]:
                max_idx = idx
                count = 0
            count += 1
            if count == k:
                return max_idx

        return max_idx

