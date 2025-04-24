import re


class Solution:
    
    def detectCapitalUse(self, word: str) -> bool:

        return re.search(r"^[A-Z]*$|^[a-z]*$|^[A-Z][a-z]*$", word) is not None
        
