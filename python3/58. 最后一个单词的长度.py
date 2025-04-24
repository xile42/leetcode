class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        
##        return len(s.strip().split(" ")[-1])
        import re

        results = re.split(r"[\s]+", s)
        for i in results[::-1]:
            if len(i) != 0:
                return len(i)
