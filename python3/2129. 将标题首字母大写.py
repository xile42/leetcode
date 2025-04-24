class Solution:

    def capitalizeTitle(self, title: str) -> str:

        ws = title.split(" ")
        results = list()
        for w in ws:
            if len(w) <= 2:
                results.append(w.lower())
            else:
                results.append(w[0].upper() + w[1:].lower())

        return " ".join(results)
