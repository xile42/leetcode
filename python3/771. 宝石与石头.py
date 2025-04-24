class Solution:
    
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        c = Counter(stones)
        result = sum([c[k] for k in jewels])

        return result
        
