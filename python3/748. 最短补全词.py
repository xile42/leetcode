class Solution:
    
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:

        licensePlate = licensePlate.lower()
        s = str()
        for c in licensePlate:
            if (not c.isdigit()) and c != " ":
                s += c
        c = Counter(s)

        ws = [[word, idx] for idx, word in enumerate(words)]
        ws = sorted(ws, key=lambda x: [len(x[0]), x[1]])
        for w, _ in ws:
            if Counter(w.lower()) >= c:
                return w
        
