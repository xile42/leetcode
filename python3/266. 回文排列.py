class Solution:

    def canPermutePalindrome(self, s: str) -> bool:

        c = Counter(s)
        chance = True
        for v in c.values():
            if v & 1 != 0:
                if chance:
                    chance = False
                else:
                    return False
        return True
        
