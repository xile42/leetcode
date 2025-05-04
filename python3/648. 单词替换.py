class Solution:

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        dictionary.sort()
        ans = list()
        for w in sentence.split(" "):
            res = None
            for pre in dictionary:
                if w.startswith(pre):
                    if res is None or len(pre) < len(res):
                        res = pre
            ans.append(w if res is None else res)

        return " ".join(ans)
