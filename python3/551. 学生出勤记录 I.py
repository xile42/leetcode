class Solution:
    
    def checkRecord(self, s: str) -> bool:

        if Counter(s)["A"] >= 2:
            return False

        for idx in range(len(s)-2):
            if s[idx] == "L" and s[idx+1] == "L" and s[idx+2] == "L":
                return False

        return True
