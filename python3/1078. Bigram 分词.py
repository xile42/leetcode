class Solution:
    
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        ws = text.split(" ")
        results = list()
        for idx in range(2, len(ws)):
            if ws[idx - 2:idx] == [first, second]:
                results.append(ws[idx])

        return results
