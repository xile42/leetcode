class Solution:
    
    def isArmstrong(self, n: int) -> bool:

        sn = str(n)
        l = len(sn)
        result = 0
        for char in sn:
            result += pow(int(char), l)

        return n == result
        
