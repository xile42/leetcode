class Solution:

    def reorderSpaces(self, text: str) -> str:

        ws = [w for w in text.split(" ") if len(w) > 0]
        w_cnt = len(ws) - 1
        b_cnt = Counter(text)[" "]

        if w_cnt == 0:
            return ws[0] + " " * b_cnt
        
        d, r = divmod(b_cnt, w_cnt)

        result = (" " * d).join(ws) + " " * r

        return result
