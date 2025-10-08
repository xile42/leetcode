class Solution:

    def discountPrices(self, sentence: str, discount: int) -> str:

        ans = list()
        ws = sentence.split(" ")

        for w in ws:
            if len(w) > 1 and w[0] == "$" and w[1:].isdigit():
                price = float(w[1:])
                price -= price * discount / 100
                ans.append(f"${price:.2f}")
            else:
                ans.append(w)

        return " ".join(ans)
